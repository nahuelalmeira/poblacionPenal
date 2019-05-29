### Diplomatura AACSyA 2019 - FaMAF - UNC

## Trabajo de mentoría anual:
# Población Penitenciaria en Argentina 2002 a 2017

facilita: Franco Camporeale

### Motivación

Para desarrollar políticas públicas el Estado necesita datos que provean la información necesaria para dimensionar y entender los problemas a tratar, así como las herramientas adecuadas para extraerla y presentarla de la forma más clara posible.

En este trabajo, utilizaremos datos del Ministerio de Justicia y DDHH para analizar la [emergencia penitenciaria](http://aaip.gob.ar/normativa/nacional/resoluci%C3%B3n-184-2019-321392/texto) declarada por el gobierno argentino en 2019, usando distintas herramientas estadísticas y algoritmos de aprendizaje automático para describir los aspectos más complejos y encontrar correlaciones, que puedan resultar de interés para el análisis de la situación del sistema carcelario nacional.

### Descripción del dataset

El Ministerio de Justicia y DDHH publica desde 2002 los datos estadísticos de la población en las cárceles del país. El dataset con el que trabajaremos está extraído del [Sistema Nacional de Estadísticas sobre la Ejecución de Penas](https://datos.gob.ar/dataset/justicia-sistema-nacional-estadisticas-sobre-ejecucion-pena---sneep) (SNEEP), y cuenta con las siguientes características:

* Estadísticas por cada año desde 2002 a 2017 inclusive. 
* El dataset unificado tiene 939728 registros. 
* El último año censado lista un total de 85283 personas. 
* Datos anónimos individuales de todos los internos de las cárceles del país. 

Por cada interno se detalla: 

* Datos de la institución: nombre, provincia, tipo de servicio
* Datos socioeconómicos: género, edad, nacionalidad, nivel de instrucción, situación laboral al ingresar, etc.
* Datos judiciales: situación legal, tipo de delito, jurisdicción, etc.
* Datos de situación en la institución: participación en programas laborales, calificación conducta, horas de trabajo remunerado, etc.
* Datos de la condena: duración de la condena, reducción de pena, salidas transitorias, etc.

Son 48 variables en total, la gran mayoría de las mismas son categóricas, con pocos casos de variables numéricas (duración de la pena, edad) y fechas (fecha de detención, fecha de condena).

El dataset se encuentra en formato CSV, para la primer materia utilizaremos una versión preprocesada del mismo y un Notebook con las instrucciones para leerlo. Para la materia de Análisis y Curación de Datos trabajaremos con el dataset original con el objetivo de que los integrantes del grupo puedan realizar el preprocesamiento de los datos.

### Práctico de Análisis y Visualización

**Objetivo y alcance**: Uso de estadísticas descriptivas para el análisis del set de datos, responder a distintas preguntas generales respecto al dataset, por ejemplo:

* Distribución por instituciones
* Distribución por rangos de edades
* Distribución por tipos de condenas
* Crecimiento de la población de 2002 a 2017 

Análisis probabilístico de distintas variable, por ejemplo:

* Probabilidad de que un interno haya sido lesionado por otro interno dado que se encuentra en un establecimiento particular.

**Método**: Presentación de un informe en formato pdf, html o md donde se detalle el estudio realizado sobre el dataset y se describan distintos aspectos de los datos. Uso de estadísticas descriptivas: Moda, media, mediana y desviación estándar. Análisis de outliers. Uso de librerías como Matplotlib y Seaborn para el graficado de datos.