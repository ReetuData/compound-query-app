import os
os.environ["OPENAI_API_KEY"] = "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"


# Importing OpenAI 
from langchain.llms import OpenAI
# Initializing an OpenAI model
llm = OpenAI(temperature=0.7)
# Creating a text
text = "What are the 5 most expensive capital cities?"
# Getting a prediction from the language model
llm(text)


