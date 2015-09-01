import os, pydicom
from django.core.management.base import BaseCommand, CommandError
from data_base.models import Group, Tag, User, Feed, Patient, Study, Data, Series, MR_Params, US_Params, CT_Params, Review, Token





class Command(BaseCommand):
    help = 'that does my stuff'


    def handle(self, *args, **options):

       for dossier, sous_dossiers, fichiers in os.walk('/neuro/users/chris/data'):
           for fichier in fichiers:
               fullpath = os.path.join(dossier, fichier)

               print(fullpath)
               try:
                  ds = pydicom.read_file(fullpath)


                  ############# Study table ##############
                  try:
                      b = Study(Name=ds.Name, Pathology=ds.Pathology, StationName=ds.StationName,
                       ManufacturerModelName=ds.ManufacturerModelName, BodyPartExaminated=ds.BodyPartExaminated,
                        MagneticFieldStrength=ds.MagneticFieldStrength, Modality=ds.Modality, StudyInstanceUID=ds.StudyInstanceUID)
                      b.save()

                  except NameError:
                      print('not possible to know this information')
                  except AttributeError:
                      print('not possible to know this information')



                      #############  table ##############


                  try:
                      b = Patient(PatientName=ds.PatientName, StudyInstanceUID=ds.StudyInstanceUID, PatientBirthdate=ds.PatientBirthdate, PatientAge=ds.PatientAge, PatientId=ds.PatientId)
                      b.save()

                  except NameError:
                      print('not possible to know this information')
                  except AttributeError:
                      print('not possible to know this information')




                      ############# Series table ##############


                  try:
                      b = Series( Name=ds.Name, SeriesName=ds.SeriesName, SeriesInstanceUID=ds.SeriesInstanceUID, ProtocolName=ds.ProtocolName)
                      b.save()

                  except NameError:
                      print('not possible to know this information')
                  except AttributeError:
                      print('not possible to know this information')





                      ############# MR_Params table ##############



                  try:
                      b = MR_Params(Name=ds.Name, SliceThickness=ds.SliceThickness, EchoTime=ds.EchoTime, InversionTime=ds.InversionTime, RepetionTime=ds.RepetionTime)
                      b.save()

                  except NameError:
                      print('not possible to know this information')
                  except AttributeError:
                      print('not possible to know this information')



                      ############# US_Params table ##############

                  try:
                      b = US_Params(Name=ds.Name)
                      b.save()

                  except NameError:
                      print('not possible to know this information')
                  except AttributeError:
                      print('not possible to know this information')


                       ############# CT_Params table ##############

                  try:
                      b = CT_Params(Name=ds.Name)
                      b.save()

                  except NameError:
                      print('not possible to know this information')
                  except AttributeError:
                      print('not possible to know this information')



                      ############# Data table ##############

                  try:
                      b = Data(Name=ds.Name, Description=ds.Description, Time=ds.Time, NbFiles=ds.NbFiles, Progress=ds.Progress)
                      b.save()

                  except NameError:
                      print('not possible to know this information')
                  except AttributeError:
                      print('not possible to know this information')



               except pydicom.errors.InvalidDicomError:
                       print('not possible to know this information')
