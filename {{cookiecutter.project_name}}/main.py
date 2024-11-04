import yaml
from src.data_ingestion import load_data
from src.preprocessing import preprocess_data
from src.model_training import train_model
from src.evaluation import evaluate_model

# Load configuration
with open("config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Data Ingestion
data = load_data(config['data']['train_path'])

# Preprocessing
processed_data = preprocess_data(data)

# Model Training
model = train_model(processed_data.drop('target', axis=1), processed_data['target'])

# Evaluation
results = evaluate_model(model, processed_data.drop('target', axis=1), processed_data['target'])
print("Model Evaluation Results:", results)
