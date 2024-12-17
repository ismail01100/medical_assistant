from .models import Symptom, Disease


def chatbot_conversation(symptom_inputs):
    """
    Fonction de base pour la conversation avec le chatbot.
    `symptom_inputs` est une liste de symptômes fournis par l'utilisateur.
    """
    matching_diseases = []

    # Cette fonction compare les symptômes fournis par l'utilisateur avec les symptômes connus
    for symptom_input in symptom_inputs:
        matching_symptoms = Symptom.objects.filter(name__icontains=symptom_input)
        
        if matching_symptoms.exists():
            for symptom in matching_symptoms:
                diseases = Disease.objects.filter(symptoms__in=[symptom])
                matching_diseases.extend(diseases)
    
    # Affichage des maladies possibles en fonction des symptômes
    if matching_diseases:
        return list(set(matching_diseases))  # Retourne les maladies sans doublons
    else:
        return "Aucune maladie trouvée correspondant aux symptômes fournis."
