

# Create your models here.
from django.db import models


class Patient(models.Model):
    PatientID = models.CharField(max_length=200,null=False)
    PatientName = models.CharField(max_length=200,null=False)
    PatientAge = models.CharField(max_length=200,default='')
    PatientSex = models.CharField(max_length=200,default='')
    PatientBirthDate = models.CharField(max_length=200,default='')
    PatientBirthTime = models.CharField(max_length=200,default='')

    def __str__(self):              # __unicode__ on Python 2
        return self.PatientID


class Study(models.Model):
    StudyDescription = models.CharField(max_length=200,null=False)
    StationName = models.CharField(max_length=200,null=False)
    ManufacturerModelName = models.CharField(max_length=200,null=False)
    StudyInstanceUID = models.CharField(max_length=200,null=False)
    Pathology = models.CharField(max_length=200,default='')
    StudyDate = models.CharField(max_length=200,default='')
    StudyTime = models.CharField(max_length=200,default='')
    AccessionNumber = models.CharField(max_length=200,default='')
    InstitutionName = models.CharField(max_length=200,default='')
    ReferringPhysicianName =models.CharField(max_length=200,default='')
    PerformingPhysicianName = models.CharField(max_length=200,default='')
    ModalitiesInStudy = models.CharField(max_length=200,default='')
    MagneticFieldStrength = models.IntegerField(default=0)
    patient = models.ForeignKey(Patient)

    def __str__(self):
        return self.StudyInstanceUID




class Series(models.Model):
    SeriesNumber = models.CharField(max_length=200,null=False)
    SeriesInstanceUID = models.CharField(max_length=200,null=False)
    ProtocolName = models.CharField(max_length=200,null=False)
    Modality = models.CharField(max_length=200,null=False)
    #AccessionNumber = models.CharField(max_length=200,default='')
    SeriesDescription = models.CharField(max_length=200,default='')
    SeriesTime = models.CharField(max_length=200,default='')
    ContrastAgent = models.CharField(max_length=200,default='')
    ScanningSequence = models.CharField(max_length=200,default='')
    BodyPartExaminated = models.CharField(max_length=200,default='')
    AcquisitionNumber =  models.CharField(max_length=200,default='')
    study = models.ForeignKey(Study)

    def __str__(self):
        return self.SeriesInstanceUID


class MR_Params(models.Model):
    PixelSpacing = models.CharField(max_length=200,default='')
    SliceThickness = models.CharField(max_length=200,default='')
    EchoTime = models.CharField(max_length=200,default='')
    EchoNumbers = models.CharField(max_length=200,default='')
    InversionTime = models.CharField(max_length=200,default='')
    RepetitionTime = models.CharField(max_length=200,default='')
    modality_params = models.OneToOneField(Series, primary_key=True)



class US_Params(models.Model):
    Name = models.CharField(max_length=200,default='')
    modality_params = models.OneToOneField(Series, primary_key=True)

    def __str__(self):
        return self.Name


class CT_Params(models.Model):
    Name = models.CharField(max_length=200,default='')
    modality_params = models.OneToOneField(Series, primary_key=True)

    def __str__(self):
        return self.Name


class Review(models.Model):
    Name = models.CharField(max_length=200,default='')
    Comment = models.CharField(max_length=200,default='')
    Rating = models.BigIntegerField()
    study = models.ForeignKey(Study)
    serie = models.ForeignKey(Series)

    def __str__(self):
        return self.Name
