import streamlit as st
from api_key import environ
from pandasai_helpers import load_df_from_duckdb, query_df

# API Key
openai_api_key = environ['OPENAI_API_KEY']

# Title for Streamlit App
st.markdown("<h1 style='text-align:center'> CHEMBL DataFrame QA App </h1>", unsafe_allow_html=True)

# View the CHEMBL DataFrame
chembl_df = load_df_from_duckdb()

# View the DataFrame and use_container_width should be True
st.dataframe(chembl_df, use_container_width=True)

### Create a prompt
prompt = st.text_input("Type in a prompt to query the CHEMBL compounds data: ", placeholder='Show me all the compounds that have SMILES strings.')

### Query using pandasai LLM
result_df = query_df(chembl_df, openai_api_key, prompt)

st.write(result_df)
