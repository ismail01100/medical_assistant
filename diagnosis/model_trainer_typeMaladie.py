from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import joblib

# Charger les données
file_path = 'data/Disease_symptom_and_patient_profile_dataset.csv'
dataset = pd.read_csv(file_path)

# Afficher les colonnes pour vérifier leur nom (optionnel)
print("Colonnes du dataset :", dataset.columns)

# Encoder les colonnes catégorielles
label_encoders = {}
for col in ['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing', 
            'Blood Pressure', 'Cholesterol Level', 'Gender']:
    le = LabelEncoder()
    dataset[col] = le.fit_transform(dataset[col])
    label_encoders[col] = le

# Cible : La colonne "Disease" qui contient les noms des maladies
target_encoder = LabelEncoder()
dataset['Disease'] = target_encoder.fit_transform(dataset['Disease'])

# Séparer les caractéristiques et la cible
X = dataset[['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing', 
             'Age', 'Gender', 'Blood Pressure', 'Cholesterol Level']]
y = dataset['Disease']

# Diviser les données en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entraîner le modèle pour prédire le type de maladie
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Sauvegarder le modèle et l'encodeur cible
joblib.dump(model, 'diagnosis/saved_model/type_disease_model.pkl')
joblib.dump(target_encoder, 'diagnosis/saved_model/type_disease_encoder.pkl')

print("Modèle pour prédire le type de maladie sauvegardé avec succès.")
