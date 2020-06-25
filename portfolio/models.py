from django.db import models

# Create your models here.


class Contact(models.Model):
	name= models.CharField(max_length=70)
	email= models.EmailField()
	message= models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Student(models.Model):
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)


	def __str__(self):
		return self.first_name