import duckdb
from os import getcwd, chdir
chdir('..')

# Connect
connection = duckdb.connect('chembl_compounds.db').cursor()

# SQL Result
df = connection.execute('SELECT * FROM chembl_compounds').df()

print(df.head())
