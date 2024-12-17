import joblib
from django.shortcuts import render
import pandas as pd
from .models import Medication

# Charger les modèles sauvegardés et l'encodeur
outcome_model = joblib.load('diagnosis/saved_model/outcome_model.pkl')
disease_model = joblib.load('diagnosis/saved_model/disease_model.pkl')
disease_label_encoder = joblib.load('diagnosis/saved_model/disease_label_encoder.pkl')

def predict_disease(request):
    result = None  # Résultat malade/non malade
    disease_name = None  # Nom de la maladie prédite
    recommended_medication = None  # Médicament recommandé

    if request.method == 'POST':
        try:
            # Récupérer les données du formulaire
            input_data = pd.DataFrame({
                'Fever': [int(request.POST['Fever'])],
                'Cough': [int(request.POST['Cough'])],
                'Fatigue': [int(request.POST['Fatigue'])],
                'Difficulty Breathing': [int(request.POST['Difficulty Breathing'])],
                'Age': [int(request.POST['Age'])],
                'Gender': [int(request.POST['Gender'])],
                'Blood Pressure': [int(request.POST['Blood Pressure'])],
                'Cholesterol Level': [int(request.POST['Cholesterol Level'])]
            })

            # Débogage des données d'entrée
            print("Input Data for Prediction:")
            print(input_data)

            # Prédiction malade/non malade
            outcome_prediction = outcome_model.predict(input_data)[0]
            print("Outcome Prediction:", outcome_prediction)

            # Décoder le résultat malade/non malade
            result = 'Malade' if outcome_prediction == 1 else 'Non malade'

            # Si Malade, prédire la maladie spécifique
            if outcome_prediction == 1:
                disease_prediction = disease_model.predict(input_data)[0]
                print("Disease Prediction (Encoded):", disease_prediction)

                # Décoder le nom de la maladie
                disease_name = disease_label_encoder.inverse_transform([disease_prediction])[0]
                print("Disease Prediction (Decoded):", disease_name)

                # Rechercher le médicament recommandé
                try:
                    medication = Medication.objects.get(disease=disease_name)
                    recommended_medication = medication.medication
                except Medication.DoesNotExist:
                    recommended_medication = "Aucune recommandation trouvée"

        except Exception as e:
            result = f"Erreur : {str(e)}"

    # Retourner les résultats dans le template
    return render(request, 'diagnosis/predict_disease.html', {
        'result': result,
        'disease_name': disease_name,
        'recommended_medication': recommended_medication
    })




from .chatbot import chatbot_conversation

def home(request):
    return render(request, 'diagnosis/home.html')
# Vue existante pour chatbot (si elle existe)
def chatbot_view(request):
    if request.method == 'POST':
        symptoms = request.POST.getlist('symptoms')  # Récupérer les symptômes
        result = chatbot_conversation(symptoms)  # Appel de la fonction chatbot_conversation
        return render(request, 'chatbot_result.html', {'result': result})
    return render(request, 'chatbot_form.html')



