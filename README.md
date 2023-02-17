# ML project
This is a notebook on our ML project.


Topic: Real estate agent's recommendations for a customer (buyer), based on data about house units sold in one year.

Team: Christopher Hedemann, Stephen Kelly, Sarah Wiesner

Bootcamp: neuefische Data Science 01/2023

## Contents

This repository contains the Jupyter notebooks [ML project](./ml_project_notebook.ipynb) and [ML model training](./ml_model_training.ipynb)as its main items. In these notebook, all the data work, including cleaning, analysis, modelling and visualization is collected. 

Furthermore, you can find the [presentation](./Abofa.pdf) given within the neuefische DS bootcamp on February 17 2023.


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
