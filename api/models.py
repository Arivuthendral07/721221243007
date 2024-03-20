from django.db import models

# Create your models here.
class company(models.Model):
    companyName=models.CharField(max_length=200)
    clientID=models. CharField(max_length=500)
    clientSecret=models.CharField(max_length=200)
    ownerEmail=models.EmailField(max_length=200)
    rollNo=models.IntegerField(max_length=1000)

