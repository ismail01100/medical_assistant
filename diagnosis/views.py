import joblib
from django.shortcuts import render
import pandas as pd
from .chatbot import chatbot_conversation
from django.shortcuts import render

# Charger le modèle sauvegardé
model_file = 'diagnosis/saved_model/random_forest_model.pkl'
model = joblib.load(model_file)


def home(request):
    return render(request, 'diagnosis/home.html')
    # Vue pour la prédiction basée sur les symptômes
def predict_disease(request):
    result = None  # Par défaut, aucun résultat n'est affiché
    if request.method == 'POST':
        try:
            # Récupérer les données du formulaire avec les noms exacts du formulaire HTML
            fever = int(request.POST['Fever'])
            cough = int(request.POST['Cough'])
            fatigue = int(request.POST['Fatigue'])
            breathing = int(request.POST['Difficulty Breathing'])
            age = int(request.POST['Age'])
            gender = int(request.POST['Gender'])
            blood_pressure = int(request.POST['Blood Pressure'])
            cholesterol = int(request.POST['Cholesterol Level'])

            # Créer un DataFrame pour le modèle
            input_data = pd.DataFrame({
                'Fever': [fever],
                'Cough': [cough],
                'Fatigue': [fatigue],
                'Difficulty Breathing': [breathing],
                'Age': [age],
                'Gender': [gender],
                'Blood Pressure': [blood_pressure],
                'Cholesterol Level': [cholesterol]
            })

            # Prédire le résultat
            prediction = model.predict(input_data)
            result = 'Positive' if prediction[0] == 0 else 'Negative'

        except KeyError as e:
            # Gérer le cas où un champ est manquant
            result = f"Erreur : Champ manquant dans le formulaire ({e})"

    # Afficher le résultat ou le formulaire vide
    return render(request, 'diagnosis/predict_disease.html', {'result': result})



# Vue existante pour chatbot (si elle existe)
def chatbot_view(request):
    if request.method == 'POST':
        symptoms = request.POST.getlist('symptoms')  # Récupérer les symptômes
        result = chatbot_conversation(symptoms)  # Appel de la fonction chatbot_conversation
        return render(request, 'chatbot_result.html', {'result': result})
    return render(request, 'chatbot_form.html')



# Vue existante pour chatbot (si elle existe)
def chatbot_view(request):
    if request.method == 'POST':
        symptoms = request.POST.getlist('symptoms')  # Récupérer les symptômes
        result = chatbot_conversation(symptoms)  # Appel de la fonction chatbot_conversation
        return render(request, 'chatbot_result.html', {'result': result})
    return render(request, 'chatbot_form.html')