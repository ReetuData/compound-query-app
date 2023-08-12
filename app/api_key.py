from json import load
from os import getcwd, environ

# Get the path to the keys.json
keys_path = getcwd()

# Create a context manager
with open(f'{keys_path}/keys.json', "r") as f:
    # Load the file as a result
    result = load(f)

# Update your environment variables
environ.update(result)

# Clear keys,values from the result dictionary
result.clear()