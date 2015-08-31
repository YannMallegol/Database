#-*- coding: utf-8 -*-

from django.db import models

class Group(models.Model):
    Name = models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.Name


class Tag(models.Model):
    Name = models.CharField(max_length=200,null=False)
    Color = models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.Name


class User(models.Model):
    Name = models.CharField(max_length=200,null=False)
    Password = models.CharField(max_length=200,null=False)
    Email = models.EmailField(max_length=200,null=False)
    group = models.ManyToManyField(Group)

    def __str__(self):
        return self.Name


class Feed(models.Model):
    Name = models.CharField(max_length=200,null=False)
    Time = models.DateTimeField(auto_now=True,null=False)
    Status = models.FloatField(null=False)
    Duration = models.BigIntegerField(null=False)
    Visible = models.BooleanField(default=False)
    user = models.ForeignKey(User)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.Name


class Patient(models.Model):
    PatientName = models.CharField(max_length=200)
    PatientSex = models.CharField(max_length=200)
    PatientBirthdate = models.DateField()
    PatientAge = models.IntegerField(default=0)
    PatientId = models.CharField(max_length=200)

    def __str__(self):
        return self.PatientName


class Study(models.Model):
    Name = models.CharField(max_length=200,null=False)
    Pathology = models.CharField(max_length=200,null=False)
    StationName = models.CharField(max_length=200,null=False)
    ManufacturerModelName = models.CharField(max_length=200,null=False)
    BodyPartExaminated = models.CharField(max_length=200)
    MagneticFieldStrength = models.IntegerField(default=0)
    Modality = models.CharField(max_length=200,null=False)
    StudyInstanceUID = models.CharField(max_length=200,null=False)
    patient = models.ForeignKey(Patient)

    def __str__(self):
        return self.Name


class Data(models.Model):
    Name = models.CharField(max_length=200,null=False)
    Description = models.CharField(max_length=200,null=False)
    Time = models.DateTimeField(auto_now=True,null=False)
    NbFiles = models.BigIntegerField(null=False)
    Progress = models.BigIntegerField(null=False)
    user = models.ManyToManyField(User)
    patient = models.ForeignKey(Patient)
    study = models.ForeignKey(Study)
    feed = models.ManyToManyField(Feed)

    def __str__(self):
        return self.Name


class Series(models.Model):
    Name = models.CharField(max_length=200,null=False)
    SeriesName = models.CharField(max_length=200,null=False)
    SeriesInstanceUID = models.CharField(max_length=200,null=False)
    ProtocolName = models.CharField(max_length=200,null=False)
    study = models.ForeignKey(Study)
    data = models.OneToOneField(Data)

    def __str__(self):
        return self.Name


class MR_Params(models.Model):
    Name = models.CharField(max_length=200)
    SliceThickness = models.IntegerField(default=0)
    EchoTime = models.FloatField(default=0)
    InversionTime = models.IntegerField(default=0)
    RepetionTime = models.IntegerField(default=0)
    modality_params = models.OneToOneField(Series)

    def __str__(self):
        return self.Name


class US_Params(models.Model):
    Name = models.CharField(max_length=200)
    modality_params = models.OneToOneField(Series)

    def __str__(self):
        return self.Name


class CT_Params(models.Model):
    Name = models.CharField(max_length=200)
    modality_params = models.OneToOneField(Series)

    def __str__(self):
        return self.Name


class Review(models.Model):
    Name = models.CharField(max_length=200)
    Comment = models.CharField(max_length=200)
    Rating = models.BigIntegerField()
    study = models.ForeignKey(Study)

    def __str__(self):
        return self.Name


class Token(models.Model):
    Value = models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.Value
