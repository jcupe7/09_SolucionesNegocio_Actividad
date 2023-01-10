import pandas as pd

# Read the data, path prepared for Power BI
dfnt_raw = pd.read_csv('D:\DOCUMENTOS HDD\VIU_Master_DS\1 - Asignaturas\09 - Soluciones de inteligecia de neocio\Actividades\09_SolucionesNegocio_Actividad\src\23100022PowerPlant.csv')


# Get only columns we want to work with
key = ['REF_DATE', 'Airports', 'Type of power plant', 'VALUE']
df = dfnt_raw[key]

# Get fata from 2012-2016
dfd = df.loc[df['REF_DATE']>=2012]

# Pivot table
Mycolumn='Type of power plant'
dataframe=dfd.pivot_table(index= ['REF_DATE','Airports'], columns= Mycolumn, values='VALUE')
dataframe.reset_index(inplace=True)
