# Cookiecutter Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work at Farmers Edge._


### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter https://github.com/jacobwbengtson/jake_cookiecutter


[![asciicast](https://asciinema.org/a/9bgl5qh17wlop4xyxu9n9wr02.png)](https://asciinema.org/a/9bgl5qh17wlop4xyxu9n9wr02)


### The resulting directory structure
------------

The directory structure of your new project looks like this:

```
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
```

## Contributing

We welcome contributions! [See the docs for guidelines](https://drivendata.github.io/cookiecutter-data-science/#contributing).

### Installing Anaconda Environment
------------

    conda env create -f environment.yml
