from django.urls import path
from .views import chatbot_view, predict_disease
from . import views  # Import du module views dans le même répertoire

urlpatterns = [
    path('chatbot/', chatbot_view, name='chatbot_view'),
    path('predict/', predict_disease, name='predict_disease'),
    path('', views.home, name='home'),  # Page d'accueil
]
