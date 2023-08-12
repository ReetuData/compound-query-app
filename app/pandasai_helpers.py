import numpy as np
import pandas as pd
import duckdb
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
from typing import Optional, Union
from duckdb_helpers import setup_duckdb_connection
from sqlalchemy import text
from os import chdir

# Change working directory
chdir("../../..")

# DataFrame Creation
def create_df(m: int, n: int) -> pd.DataFrame:
    """
    Arguments:
        - m (integer): Number of rows
        - n (integer) : Number of columns
    
    Output:
        - df (pandas DataFrame): Synthetically generated pandas DataFrame from numpy.random

    """
    # Create a random numpy array of integers
    arr = np.random.randint(0, 10000, size=(m,n))

    # Convert the Array into a Pandas DataFrame
    df = pd.DataFrame(arr)

    # Change the Column Names based on the number of columns
    df.columns = [f'col_{i+1}' for i in range(n)]

    return df

# Load chembl_df from duckdb
def load_df_from_duckdb(db_name='chembl_compounds.db', query='SELECT * from chembl_compounds'):
    connection = duckdb.connect(db_name)

    result = duckdb.sql(query, connection=connection).df()

    return result

# Load chembl_df
def load_df_from_duckdb_connection(db_name='chembl_compounds.db', query='SELECT * from chembl_compounds'):
    # SQLAlchemy connection object
    cursor = setup_duckdb_connection(db_name).connect()

    # Transform query string into executable SQL query representation in Python
    query_exec = text(query)

    # Read the chembl_compounds table
    df = pd.read_sql_query(query_exec, con=cursor)

    # Closing the cursor
    cursor.close()

    print(f"Connection to {db_name} closed successfully. Transaction completed.")

    return df

# Function to query a DataFrame using Pandas AI
def query_df(df: pd.DataFrame, api_key:str, prompt: str) -> Union[Optional[pd.DataFrame], Optional[str]]:
    """
    Arguments:
        - df (pandas DataFrame): Input DataFrame that provides context for PandasAI
        - api_key (string): Secret credential required by OpenAI in order to use the GPT model for pandas-ai
        - prompt (string): The actual prompt that is passed by the end user to get answers from the DataFrame

    Output:
        - result (DataFrame or string): Result that comes out of the OpenAI model based on an input prompt.
        
    """
    # Instantiate OpenAI Model
    openai = OpenAI(api_key)

    # PandasAI llm object
    llm = PandasAI(openai)

    # Result Variable
    result = llm(df, prompt)

    return result