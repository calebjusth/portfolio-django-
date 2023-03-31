from django.db import models

# Create your models here.

class Brands(models.Model):
	image = models.ImageField()


class Service(models.Model):
	text = models.CharField(max_length=40)
	details = models.CharField(max_length=60, default="backed up with AI power and machine Learning")
	image = models.ImageField()
	def __str__(self):
		return self.text

class Testimonials(models.Model):
	testimoney = models.TextField()
	name =  models.CharField(max_length=100)
	position_of_client = models.CharField(max_length=200,default="Worker")
	campany_name = models.CharField(max_length=200, default="")
	image = models.FileField(upload_to="testimonials vid and img")
	def __str__(self):
		return self.name

class Other_Testimonials(models.Model):
	testimoney = models.TextField()
	name = models.CharField(max_length=100)
	position_of_client = models.CharField(max_length=200, default="worker")
	company_name = models.CharField(max_length=200, default="")
	image = models.FileField()
	def __str__(self) -> str:
		return self.testimoney[10]


class Work(models.Model):
	Title = models.CharField(max_length=100)
	detail = models.CharField(max_length=100, default="")
	image = models.ImageField()
	link = models.CharField(max_length=200, default="")
	
	def __str__(self):
		return self.Title