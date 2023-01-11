from IPython.display import display
import pandas as pd

# Read the data, path prepared for Power BI
dfnt_raw = pd.read_csv('D:\\DOCUMENTOS HDD\\VIU_Master_DS\\1 - Asignaturas\\09 - Soluciones de inteligecia de neocio\\Actividades\\09_SolucionesNegocio_Actividad\\src\\23100022PowerPlant.csv')
#dfnt_raw = pd.read_csv('23100022PowerPlant.csv')
# Get only columns we want to work with
key = ['REF_DATE', 'Airports', 'Type of power plant', 'VALUE']
df = dfnt_raw[key]

# Get fata from 2012-2016
dfd = df.loc[df['REF_DATE']>=2012]

# Pivot table
Mycolumn='Type of power plant'
df = dfd.pivot_table(index= ['REF_DATE','Airports'], columns= Mycolumn, values='VALUE')
df.reset_index(inplace=True)

# Get 'All Airports' data in a df
mask = df['Airports'] == 'Total, all airports'
df_all = df[mask]

# Get each airport data in a df
mask = df['Airports'] != 'Total, all airports'
df_ap = df[mask]

# Split Airports into AirportName and State
df_ap[['Airport','State']] = df_ap['Airports'].str.split(',',expand=True)
df_ap = df_ap.drop(['Airports', 'Airport'], axis=1)


#Group by state and year
df_states = df_ap.groupby(['REF_DATE', 'State']).sum()
df_states.reset_index(inplace=True)

display(df_states)