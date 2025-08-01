from django.db import models

# Create your models here.
class election (models.Model):
    name=models.CharField(max_length=10)
    father_name=models.CharField(max_length=15)
    date_of_birth=models.DateField()
    house_name=models.CharField(max_length=20)
    ward_number=models.IntegerField()
   
    