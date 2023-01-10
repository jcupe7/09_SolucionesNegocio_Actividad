import pandas as pd
from IPython.display import display

# Read the data
dfnt_raw = pd.read_csv('23100022PowerPlant.csv')

# Get only columns we want to work with
key = ['REF_DATE', 'Airports', 'Type of power plant', 'VALUE']
df = dfnt_raw[key]

# Get fata from 2014-2016
dfd = df.loc[df['REF_DATE']>=2012]

# Pivot table
Mycolumn='Type of power plant'
dataframe=dfd.pivot_table(index= ['REF_DATE','Airports'], columns= Mycolumn, values='VALUE')
dataframe.reset_index(inplace=True)

display(dataframe)

