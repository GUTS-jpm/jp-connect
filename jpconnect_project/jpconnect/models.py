from django.db import models
from django.db.models import CharField

class Employees(models.Model):
    first_name = CharField(max_length=128, unique=False)
    last_name = CharField(max_length=128, unique=False)
    id = CharField(max_length=128, unique=True, primary_key=True)
    location = CharField(max_length=128, unique=False)

    def __str__(self):
        return self.id+", "+self.first_name+", "+self.last_name+", "+self.location
