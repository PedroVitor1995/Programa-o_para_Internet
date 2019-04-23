from django.db import models

# Create your models here.

class Person(models.Model):
	SHIRT_SIZES = (
		('S','Small'),
		('M','Medium'),
		('L','Larger'),
	)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	pub_date = models.DateTimeField('date published')
	shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, null=True)

class Manufacter(models.Model):
	name = models.CharField(max_length=50)

class Car(models.Model):
	name = models.CharField(max_length=50)
	manufacter = models.ForeignKey(Manufacter,on_delete=models.CASCADE,related_name='cars')

