from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Symptom(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class PatientProfile(models.Model):
    AGE_GROUP_CHOICES = [
        ('0-18', '0-18'),
        ('19-35', '19-35'),
        ('36-60', '36-60'),
        ('60+', '60+'),
    ]
    
    gender = models.CharField(max_length=6, choices=[('Male', 'Male'), ('Female', 'Female')])
    age = models.IntegerField()
    age_group = models.CharField(max_length=5, choices=AGE_GROUP_CHOICES)
    blood_pressure = models.CharField(max_length=50)
    cholesterol_level = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.gender}, {self.age} years"

class PatientSymptom(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    symptom = models.ForeignKey(Symptom, on_delete=models.CASCADE)
    presence = models.BooleanField()

class Diagnosis(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
    outcome = models.CharField(max_length=50)  # 'Positive' or 'Negative'



class Medication(models.Model):
    disease = models.CharField(max_length=100, unique=True)
    medication = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.disease} - {self.medication}"