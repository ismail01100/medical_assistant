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

# Supposons que 'Outcome Variable' est la cible (0 pour négatif, 1 pour positif)
le_outcome = LabelEncoder()
dataset['Outcome Variable'] = le_outcome.fit_transform(dataset['Outcome Variable'])

# Séparer les caractéristiques (features) et la cible
X = dataset[['Fever', 'Cough', 'Fatigue', 'Difficulty Breathing', 
             'Age', 'Gender', 'Blood Pressure', 'Cholesterol Level']]
y = dataset['Outcome Variable']

# Diviser les données en ensemble d'entraînement et ensemble de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print("Données préparées avec succès.")
print(X_train.head())

# Initialiser le modèle Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Entraîner le modèle avec les données d'entraînement
model.fit(X_train, y_train)

# Faire des prédictions sur les données de test
y_pred = model.predict(X_test)

# Évaluer le modèle
accuracy = accuracy_score(y_test, y_pred)
print(f"Précision du modèle : {accuracy * 100:.2f}%")

# Afficher un rapport de classification détaillé
print("Rapport de classification :")
print(classification_report(y_test, y_pred))
# Sauvegarder le modèle entraîné
model_file = 'diagnosis/saved_model/random_forest_model.pkl'
joblib.dump(model, model_file)
print(f"Modèle sauvegardé avec succès dans : {model_file}")