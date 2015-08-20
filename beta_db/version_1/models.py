from django.db import models

# Create your models here.


class Identity(models.Model):
    MRN_DBID_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class type_of_analyse(models.Model):
	identity = models.ForeignKey(Identity)
    DIFFUSION = models.ForeignKey(max_length=200)
    Localizer = models.CharField(max_length=200)
    MPRAGE = models.IntegerField(max_length=200)