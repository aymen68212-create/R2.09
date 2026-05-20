from django.db import models

class Espece(models.Model):
    nom = models.CharField(max_length=100)
    origine = models.CharField(max_length=100)
    est_dangereux = models.BooleanField(default=False)

    def __str__(self):
        return f"L'espèce s'appelle{self.nom}, son origine est {self.origine} et son statut de dangerosité est {self.est_dangereux}"

class Animal(models.Model):
    nom = models.CharField(max_length=100)
    age = models.IntegerField()
    espece = models.ForeignKey(Espece, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"L'animal s'appelle {self.nom}, son age est {self.age}, son espèce est {self.espece} et ca description est la suivante : {self.description}"
    