from django.db import models

from django_better_admin_arrayfield.models.fields import ArrayField

class Patient(models.Model):
    first_name = models.CharField('First_name',max_length=150, blank=True)
    last_name = models.CharField('Last_name', max_length=150, blank=True)
    diagnoses = ArrayField(
        models.CharField(max_length=255),blank=True,default=list)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Patient: ID- {self.id}, Name-{self.first_name}"
