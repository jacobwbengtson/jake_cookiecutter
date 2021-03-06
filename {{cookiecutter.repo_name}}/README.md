{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

Project Organization
------------

    ├── README.md             <- The top-level README for developers using this project.
    ├── .gitignore            <- Boiler plate version will be provided
    ├── config.txt            <- contains passwords and tokens that should not be version controlled
    ├── environment.yml       <- The .yml file used to create the envrionment for the project.
    │                         Generate .yml file using 'conda env_name export > environment.yml'.
    │                         Generate a virtual environment from .yml using 'conda env_name create -f envrionment.yml'.
    ├── data
    │   ├── processed         <- The final, canonical data sets for modeling.
    │   ├── interim           <- Data that has been cleansed or altered, but is not in its final state
    │   └── raw               <- The original, immutable data dump.
    │
    ├── models                <- Trained and serialized models, model predictions, or model summaries
    │
    ├── exploration           <- Jupyter notebooks or python scripts for EDA. Naming convention is a number
    │                            (for ordering), the creator's initials, and a short `_` delimited description, e.g.
    │                             e.g. `1.0_jwb_initial_data_exploration.ipynb`.
    │
    ├── experiments           <- Jupyter notebooks or python scripts for model experimentation. Naming convention is a number
    │                            (for ordering), the creator's initials, and a short `_` delimited description, e.g.
    │                             e.g. `1.0_jwb_random_forest.py`.
    │
    ├── references            <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── main.py               <- Script that will run everything required to generate the best working model for the project
    │                            From data ingestion to model training
    │
    │
    └── src                   <- Source code for use in this project.
        ├── __init__.py       <- Makes src a Python module
        │
        ├── data              <- Functions to download, generate, combine, clean, or featurize data.
        │   ├── pull.py       <- Outputs to data/raw
        │   ├── clean.py      <- Outputs to data/interim
        │   └── featurize.py  <- Outputs to either data/interim or data/processed
        │
        ├── models            <- Functions to train/test models, or use trained models for predictions
        │   ├── train.py
        │   ├── test.py
        │   └── predict.py
        │
        └── visualization     <- Functions to create exploratory and results oriented visualizations
            └── visualize.py



--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>