import pandas as pd
from diagnosis.models import Medication

def import_medications():
    file_path = 'Data/Disease_symptom_and_patient_profile_dataset.csv'
    recommended_medications = {
        "Influenza": "Paracétamol",
        "Common Cold": "Ibuprofène",
        "Eczema": "Corticoïdes topiques",
        "Asthma": "Ventoline (Salbutamol)",
        "Hypertension": "Amlodipine",
        "Diabetes": "Metformine",
        "Bronchitis": "Amoxicilline",
        "Pneumonia": "Azithromycine",
        "Migraine": "Ibuprofène ou Sumatriptan",
        "Tuberculosis": "Rifampicine",
    }

    # Lire le fichier CSV
    df = pd.read_csv(file_path)
    diseases = df['Disease'].unique()

    # Ajouter les médicaments dans la base de données
    for disease in diseases:
        medication = recommended_medications.get(disease, "Consultez un médecin pour recommandation")
        Medication.objects.get_or_create(disease=disease, defaults={'medication': medication})

    print("Données importées avec succès !")
