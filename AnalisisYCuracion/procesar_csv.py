import os
import sys
import pandas as pd
import numpy as np

def preprocesar_csv(input_file, output_file, year=None):
    number_of_fields = []
    with open(input_file, 'r') as in_f:
        with open(output_file, 'w') as out_f:
            line = in_f.readline()
            if year == 2017:
                line = line.replace('tiene_medidas_seguridad,', '')
                line = line.replace('recibio_atencion_medica_ult_anio,', 
                                    'recibio_atencion_medica_ult_anio_id,') #col _id mal nombrada  
            while line:
                out_line = line.replace(',TRENEL', ', TRENEL')
                out_line = out_line.replace(', ', '[COMA] ')
                out_line = out_line.replace(',', ';')
                out_line = out_line.replace('[COMA]', ',')
                out_line = out_line.replace(';"', ";")
                out_line = out_line.replace('";', ";")
                NF = len(out_line.split(';'))
                number_of_fields.append(NF)
                out_f.write(out_line)
                line = in_f.readline()
                
    assert len(np.unique(number_of_fields)) == 1

def filtrar_nulos(df, f=0.8):
    """
    Descarto registros que tengan al menos
    una fraccion f de campos nulos.
    """
    
    n_cols = df.shape[1]
    n_null = df.isnull().sum(axis=1)
    mask = n_null < int(n_cols*f)
    df = df[mask]
    return df
    

def procesar_fechas(df, current_year):
    """
    Descarto fechas que sean posteriores al 31 de Diciembre
    del año en que se realizo el censo.
    """
    
    date_cols = ['fecha_detencion', 'fecha_condenado']
    incorrect_dates = {}
    for date_col in date_cols:
        incorrect_dates[date_col] = 0
        corrected_values = []
        for i, date in df[date_col].items():
            if isinstance(date, str):
                year = int(date.split('/')[2][:4])
                if year > current_year:
                    incorrect_dates[date_col] += 1
                    date = np.NaN
                else:
                    try:
                        date = date[:10]
                    except:
                        print(date)

            corrected_values.append(date)
        df[date_col] = corrected_values

    df['fecha_detencion'] = pd.to_datetime(df['fecha_detencion'])
    df['fecha_condenado'] = pd.to_datetime(df['fecha_condenado'])
    return df

def calcular_tiempo_resolucion(df):
    """
    Creo un nuevo campo con el tiempo de resolucion de condena.
    """
    
    condenados = df['situacion_legal_descripcion'] == 'Condenado'
    df['tiempo_resolucion'] = df['fecha_condenado'] - df['fecha_detencion']
    return df

def calcular_numero_delitos(df):
    """
    Creo un nuevo campo con la cantidad de delitos cometidos.
    """
    
    delito_cols = ['delito{}_descripcion'.format(i) for i in range(1, 6)]
    df['delitos_cantidad'] = df[delito_cols].count(axis=1)
    return df

def procesar_edades(df):
    """
    Reemplazo los NaN y valores iguales a 0 por la media de las edades.
    """
    #mask = (df['edad'] == 0) & ((df['delitos_cantidad'] > 0) | \
    #                              (df['situacion_legal_descripcion'] == 'Condenado') | \
    #                              (df['nivel_instruccion_descripcion'].notnull()))
    mask = df['edad'] == 0
    df[mask] = np.NaN
    df['edad'].fillna(df['edad'].mean(skipna=True))
    return df

def eliminar_id(df):
    """
    Elimina las columnas _id, nos quedamos solo con las descripciones
    """
    df = df.drop([x for x in df if x.endswith('_id')], 1)
    df.columns = [col.replace('_descripcion', '') for col in df.columns]
    return df

#input_file = '../datasets/sneep-2017.csv'
#output_file = '../datasets/py_sneep-2017.csv'
input_file = sys.argv[1]
output_file = sys.argv[2]

if len(sys.argv) > 3:
    year = int(sys.argv[3])
else:
    year = None

print('Preprocesando csv')
preprocesar_csv(input_file, output_file, year=year)

df = pd.read_csv(output_file, sep=';')
df = filtrar_nulos(df, f=0.7)

print('Procesando fechas')
df = procesar_fechas(df, current_year=2017)
print('Calculando tiempo resolucion')
df = calcular_tiempo_resolucion(df)
print('Calculando numero de delitos')
df = calcular_numero_delitos(df)
print('Procesando edades')
df = procesar_edades(df)
print('Eliminando columnas con pocos datos')
df = filtrar_nulos(df, f=0.7)
print('Eliminando las columnas _id' )
df = eliminar_id(df)

df.to_csv(path_or_buf=output_file, sep=';')