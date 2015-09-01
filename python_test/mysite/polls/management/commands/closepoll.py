import os, pydicom
from django.core.management.base import BaseCommand, CommandError
#from data_base.models import Group, Tag, User, Feed, Patient, Study, Data, Series, MR_Params, US_Params, CT_Params, Review, Token 
from django.db import IntegrityError




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
                      print(ds.Name)
                     # b = Study(Name=ds.Name)
                     # b.save()
                                                                 
                  except NameError:
                      print('not possible to know this information')
                  except AttributeError:
                      print('not possible to know this information')
                      
                  try:
                      print(ds.Pathology)
                      #b = Study(Pathology=ds.Pathology)
                      #b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:
                      print('not possible to know this information')
                      
                      
                  try:
                      print(ds.StationName)
                      #b = Study(StationName=ds.StationName)
                     # b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:
                      print('not possible to know this information')    
                      

                    
                      
                      
               except pydicom.errors.InvalidDicomError:
                       print('not possible to know this information')
                       
