# Compound-Query-App
This application allows users to interactively query and analyze compound data sourced from the CHEMBL database


## Querying Compounds with LLMs

> This application allows users to interactively query and analyze compound data sourced from the **CHEMBL** database. By leveraging the power of `pandas-ai`, users can ask complex questions and receive insightful answers about various chemical compounds.

## Table of Contents

1. [Rationale](#rationale)
2. [Installation](#installation)
3. [Use Cases](#use-cases)


### Rationale

The motivation behind this project is to make chemical data from the CHEMBL database easily accessible and understandable. By utilizing the analytical capabilities of pandas-ai and the interactive interface of Streamlit, researchers, chemists, and enthusiasts can dig into the chemical world without the need for complicated programming or database skills.

### Demo

- Please feel free to check out the hosted demo [here](http://209.182.236.218:8060).

### Installation

Make sure you have Python 3.6+ installed on your machine. You can then follow these steps to install the required dependencies:

#### Docker

```bash
# Clone the repository
git clone https://github.com/ReetuData/compound-query-app.git

# Navigate to the application root folder
cd compound-query-app

# Run the docker-compose YML file
docker-compose up -d
```

#### Without Docker

- Run the app using:

```bash
# Clone the repository
git clone https://github.com/ReetuData/compound-query-app.git

# Navigate to the application root folder
cd compound-query-app

# Install Python module requirements
pip install -r requirements.txt

# Run the Streamlit application
streamlit run pandasai_demo.py
```

### Use Cases
- **Research and Development**: Analyze chemical compounds for potential drug discovery or educational purposes.
- **Chemical Education**: An educational tool for chemistry students to understand various chemical properties and relations.
- **Data Visualization**: Generate interactive plots and graphs for presentations and reports.
Custom Queries: Enable sophisticated query formulation to find specific information about compounds.
