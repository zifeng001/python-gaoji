from django.db import models

# Create your models here.

class School(models.Model):
	school_id = models.IntegerField()
	school_name = models.CharField(max_length=20)
	# my_manager = models.OneToOneField('Manager')
	def __str__(self):
		return self.school_name

class Manager(models.Model):
	manager_id = models.IntegerField()
	manager_name = models.CharField(max_length=20)
	my_school = models.OneToOneField(School)
	def __str__(self):
		return self.manager_name