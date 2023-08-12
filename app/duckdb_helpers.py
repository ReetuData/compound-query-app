import duckdb
import pandas as pd
from sqlalchemy import create_engine

# Setup DuckDB Connection
def setup_duckdb_connection(db_name: str):
    # URI for DUCKDB
    
    # URI for Local: ///
    # URI for Network: //

    uri = f'duckdb:///{db_name}'

    # SQLAlchemy Engine
    engine = create_engine(uri)

    return engine

# Setup DuckDB Database
def setup_duckdb_database(db_name: str, df: pd.DataFrame, table_name: str):
    # Connection
    connection = duckdb.connect(db_name)

    # Run a SQL Query
    duckdb.sql(f"CREATE TABLE {table_name} AS (SELECT * FROM df)", connection=connection)

    # Close the connection
    connection.close()
