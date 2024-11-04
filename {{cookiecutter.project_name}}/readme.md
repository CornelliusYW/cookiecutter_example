# {{ cookiecutter.project_name }}

## Overview
{{ cookiecutter.description }}

## Project Structure
├── data/
│   ├── raw/               # Raw input data
│   ├── processed/         # Preprocessed data
├── src/
│   ├── data_ingestion.py  # Data loading functions
│   ├── preprocessing.py   # Data preprocessing functions
│   ├── model_training.py  # Model training functions
│   ├── evaluation.py      # Model evaluation functions
├── models/                # Directory to save trained models
├── config/
│   ├── config.yaml        # Main configuration file
├── main.py                # Main script to run the pipeline
├── requirements.txt       # Dependencies for the project
└── README.md              # Project overview
