from django.db import models

# Create your models here.




class Patient(models.Model):
	name = models.CharField(max_length=20)
	BirthDate = models.CharField(max_length=20)
	age = models.IntegerField()
	sexe = models.CharField(max_length=20)
	size = models.IntegerField()


class Review(models.Model):
	study = models.OneToOneField(Study)
	anatomy = models.CharField(max_length=120)
	quality = models.IntegerField()


class Study(models.Model):
	
	uid = models.CharField(max_length=20)
	StudyDate = models.IntegerField()
	StudyDescription = models.CharField(max_length=20)


class Machine(models.Model):
	study = models.OneToOneField(Study)
	Software = models.CharField(max_length=120)
	ManuFacturerModelName = models.CharField(max_length=20)


class Groups(models.Model):
	uid = models.CharField(max_length=20)
	nameGroup = models.CharField(max_length=20)


class Users(models.Model):
	uid = models.CharField(max_length=20)



class Data(models.Model):
	uid = models.CharField(max_length=20)
	Description = models.CharField(max_length=20)
	name = models.CharField(max_length=20)
	acquisitionTime = models.IntegerField()
	nbFiles = models.IntegerField()
	status = models.CharField(max_length=20)
	plugin = models.CharField(max_length=20)


class Series(models.Model):	
	study = models.OneToOneField(Study)
	series = models.ForeignKey(Series)
	seriesNumber = models.IntegerField()
	seriesName = models.CharField(max_length=20)
	seriesTime = models.IntegerField()
	seriesDate = models.IntegerField()




class ExtraData(models.Model):
	data = models.OneToOneFieldData)
	positionRef = models.CharField(max_length=20)
	patientPosition = models.CharField(max_length=20)
	protocoleName = models.CharField(max_length=20)
	sliceLocation = models.CharField(max_length=20)
	sliceThickness = models.CharField(max_length=20)
	repetitionTime = models.IntegerField()
	echoTime = models.IntegerField()
	inversionTime = models.IntegerField()
	magnecticFiledStrength = models.CharField(max_length=20)


	






