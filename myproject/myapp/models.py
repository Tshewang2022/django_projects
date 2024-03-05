from django.db import models

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	contact = models.CharField(max_length=20)
	country = models.CharField(max_length=50)
	date_of_birth = models.DateField()