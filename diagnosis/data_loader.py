import pandas as pd

def load_dataset():
    file_path = 'data/Disease_symptom_and_patient_profile_dataset.csv'
    df = pd.read_csv(file_path)
    return df

# Appeler la fonction pour charger les données
dataset = load_dataset()

# Afficher les premières lignes du dataset pour vérifier
print(dataset.head())
# Afficher les colonnes du dataset
print(dataset.columns)

# Afficher des statistiques descriptives sur les données numériques
print(dataset.describe())

# Vérifier les valeurs manquantes
print(dataset.isnull().sum())