import pandas as pd
from pandasai_demo import query_df
from os import getcwd

# Data Path
data_path = getcwd() + "/data/mp2"

# Read DataFrame
df = pd.read_csv(f"{data_path}/GPCR_Receptors_Raw.csv", sep=';')

# Prompt
prompt = 'Filter the rows that are associated with humans.'

chembl_df = query_df(df, prompt)

print(chembl_df)