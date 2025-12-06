import nltk
import os

models_dir = "models"

os.makedirs(models_dir, exist_ok=True)
nltk_data_dir = os.path.join(models_dir, 'nltk_data')
os.makedirs(nltk_data_dir, exist_ok=True)
