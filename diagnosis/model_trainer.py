from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import joblib

# Charger les données
file_path = 'data/Disease_symptom_and_patient_profile_dataset.csv'
dataset = pd.read_csv(file_path)

# Encoder les colonnes catégorielles en valeurs numériques
label_encoders = {}
for col in ['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing', 
            'Blood Pressure', 'Cholesterol Level', 'Gender']:
    le = LabelEncoder()
    dataset[col] = le.fit_transform(dataset[col])
    label_encoders[col] = le

# Encodeur pour Outcome Variable et Disease
le_outcome = LabelEncoder()
dataset['Outcome Variable'] = le_outcome.fit_transform(dataset['Outcome Variable'])

le_disease = LabelEncoder()
dataset['Disease'] = le_disease.fit_transform(dataset['Disease'])

# Caractéristiques
X = dataset[['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing', 
             'Age', 'Gender', 'Blood Pressure', 'Cholesterol Level']]

# Modèle pour prédire malade/non malade
y_outcome = dataset['Outcome Variable']
X_train, X_test, y_train, y_test = train_test_split(X, y_outcome, test_size=0.3, random_state=42)

model_outcome = RandomForestClassifier(n_estimators=100, random_state=42)
model_outcome.fit(X_train, y_train)
joblib.dump(model_outcome, 'diagnosis/saved_model/outcome_model.pkl')

# Modèle pour prédire la maladie
y_disease = dataset['Disease']
X_train_disease, X_test_disease, y_train_disease, y_test_disease = train_test_split(X, y_disease, test_size=0.3, random_state=42)

model_disease = RandomForestClassifier(n_estimators=100, random_state=42)
model_disease.fit(X_train_disease, y_train_disease)
joblib.dump(model_disease, 'diagnosis/saved_model/disease_model.pkl')

# Sauvegarder le LabelEncoder pour décoder les maladies
joblib.dump(le_disease, 'diagnosis/saved_model/disease_label_encoder.pkl')
print("LabelEncoder sauvegardé pour la colonne Disease.")

print("Modèles sauvegardés avec succès.")
