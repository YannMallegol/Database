from django.db import models

# Create your models here.


class Identity(models.Model):
	MRN_DBID = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return unicode(self).encode('utf-8')

class type_of_analyse(models.Model):
	identity = models.ManyToManyField(Identity)
	DIFFUSION = models.CharField(max_length=20)
	Localizer = models.CharField(max_length=20)
	MPRAGE = models.CharField(max_length=20)
	def __str__(self):
		return unicode(self).encode('utf-8')

class age_patient(models.Model):
	identity = models.ForeignKey(Identity)
	age = models.IntegerField(default=0)
	def __str__(self):
		return unicode(self).encode('utf-8')