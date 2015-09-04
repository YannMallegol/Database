import os, pydicom
from django.core.management.base import BaseCommand, CommandError
from data_base.models import Group, Tag, User, Feed, Patient, Study, Data, Series, MR_Params, US_Params, CT_Params, Review, Token





class Command(BaseCommand):
    help = 'that does my stuff'


    def handle(self, *args, **options):

       #for dossier, sous_dossiers, fichiers in os.walk('/neuro/users/chris/data'):
        for dossier, sous_dossiers, fichiers in os.walk('/neuro/users/yann.mallegol/Documents/internship/chris-db/python_test/dicoms/0076-1.2.840.113619.2.135.2025.2078900.5939.1097298450.587.dcm'):
           for fichier in fichiers:
               fullpath = os.path.join(dossier, fichier)
               import pdb; pdb.set_trace()
               print(fullpath)
               try:

                  ds = pydicom.read_file(fullpath)
                  patient=Patient()
                  patient.PatientId=ds.PatientId
                  patient.save()
                  import pdb; pdb.set_trace()

               except pydicom.errors.InvalidDicomError:
                   print('not possible to know this information')
