import pandas as pd
from os import getcwd, listdir, chdir
from os.path import splitext
from duckdb_helpers import setup_duckdb_database, setup_duckdb_connection

# Change working directory
chdir("../../..")

# 1. Loading in the CHEMBL data
data_path = getcwd() + "/data/mp2/chembl"

# Get all the CSVs in a list
csv_files = [file for file in listdir(data_path) if splitext(file)[1] == '.csv']

# Transform each CSV file string into a pandas DataFrame
chembl_df_list = [pd.read_csv(f"{data_path}/{csv_file}", sep=';') for csv_file in csv_files]
print("List of DataFrames created successfully from CHEMBL CSV files.")

# Concatenate them into a single DataFrame
df = pd.concat(chembl_df_list)
print("DataFrame consolidated successfully.")
# 2. Setup DuckdB Database

# Create the in-memory datastore
setup_duckdb_database('chembl_compounds.db', df, 'chembl_compounds')
print("DuckDB database created successfully.")

# Setup a connection which is SQLAlchemy-compliant
duckdb_cursor = setup_duckdb_connection('chembl_compounds.db').connect()
print("duckdb-connection via SQLAlchemy connected successfully.")

# # 3. Pandas to DuckDB ETL
# df.to_sql('chembl_compounds', con=duckdb_cursor, index=False, if_exists='replace')
# print("ETL from pandas DataFrame to DuckDB table chembl_compounds completed as new table generated!")