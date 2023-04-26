# ML project
This is a notebook on our ML project for predicting air pollution in African cities. We are still cleaning things up, please come back in a week or so :-)
27.4.2023

Topic: Prediction PM10 concentrations based on weather conditions in African cities.
Team: Christopher Hedemann, Stephen Kelly, Sarah Wiesner
Bootcamp: neuefische Data Science 01/2023

## Contents

This repository contains the Jupyter notebook [ML project](./ml_project_notebook.ipynb) as its main item. In this notebook, all the data work, including cleaning, analysis, modelling and visualization is collected. 

Furthermore, you can find the [presentation](./tbd.pdf) given within the neuefische DS bootcamp.


## Requirements and Setup

- pyenv
- python==3.9.8


This repo contains a [requirements.txt](./requirements.txt) file with a list of all the packages and dependencies you will need.
For installing the virtual environment you can either use the Makefile and run `make setup` or install it manually with the following commands: 

```Bash
pyenv local 3.9.8
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

In order to train the model and store test data in the data folder and the model in models run:

```bash
#activate env
source .venv/bin/activate

python data/train.py  
```

In order to test that predict works on a test set you created run:

```bash
python data/predict.py models/linear_regression_model.sav data/X_test.csv data/y_test.csv
```

## Limitations

Development libraries are part of the production environment, normally these would be separate as the production code should be as slim as possible.
