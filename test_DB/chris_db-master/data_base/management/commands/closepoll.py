import os, pydicom
from django.core.management.base import BaseCommand, CommandError
from data_base.models import Group, Tag, User, Feed, Patient, Study, Data, Series, MR_Params, US_Params, CT_Params, Review, Token 
from django.db import connection




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
                      b = Study(Name=ds.Name)
                      b.save()
                                                                 
                  except NameError:
                      print('not possible to know this information')
                  except AttributeError:
                      print('not possible to know this information')
                      
                  try:
                      b = Study(Pathology=ds.Pathology)
                      b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:
                      print('not possible to know this information')
                      
                      
                  try:
                      b = Study(ManufacturerModelName=ds.ManufacturerModelName)
                      b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:
                      print('not possible to know this information')    
                      
                      
                  try:
                      b = Study(BodyPartExaminated=ds.BodyPartExaminated)
                      b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:
                      print('not possible to know this information')      
                      
                  
                  
                  try:
                      b = Study(MagneticFieldStrength=ds.MagneticFieldStrength)
                      b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:
                      print('not possible to know this information')      
                      
                      
                  try:
                      b = Study(Modality=ds.Modality)
                      b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:
                      print('not possible to know this information')
                      
                  try:
                      b = Study(StudyInstanceUID=ds.StudyInstanceUID)
                      b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information')
                      
                      
   
   
   
                      
                      
                      ############# Patient table ##############
                      
                      
                  try:
                      b = Patient(PatientName=ds.PatientName)
                      b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information')    
                      
                  try:                      
                      b = Patient(PatientSex=ds.PatientSex)
                      b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information')
                      
                      
                  try:                         
                      b = Patient(PatientBirthdate=ds.PatientBirthdate)
                      b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information')  
                   
                      
                  try:                         
                      b = Patient( PatientAge=ds.PatientAge)
                      b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information') 
                      
                      
                  try:                          
                      b = Patient( PatientId=ds.PatientId)
                      b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information')
                      
                      
                      
                      ############# Series table ##############
                      
                      
                  try:                          
                      b = Series( Name=ds.Name)
                      b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information')
                      
                      
                      
                  try:                          
                      b = Series( SeriesName=ds.SeriesName)
                      b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information')
                      
                      
                      
                  try:                          
                      b = Series(SeriesInstanceUID=ds.SeriesInstanceUID)
                      b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information')
                      
                      
                      
                  try:                          
                      b = Series(ProtocolName=ds.ProtocolName)
                      b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information') 
                      
                      
                  try:                          
                      b = Series(study=ds.study)
                      b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information')
                      

                      
                      
                      ############# MR_Params table ##############
                                    
                                           
                      
                      try:                          
                          b = MR_Params(Name=ds.Name)
                          b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information')
                      
                      
                      
                      try:                          
                          b = MR_Params(EchoTime=ds.EchoTime)
                          b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information')
                      
                      
                      
                      try:                          
                          b = MR_Params(InversionTime=ds.InversionTime)
                          b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information')
                      
                      
                      try:                          
                          b = MR_Params(RepetionTime=ds.RepetionTime)
                          b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information')
                      
                      
                      try:                          
                          b = MR_Params(modality_params=ds.modality_params)
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
                          b = Data(Name=ds.Name)
                          b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information')
                      
                      
                      
                     try:                                                  
                          b = Data(Description=ds.Description)
                          b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information') 
                      
                     
                     
                     try:                                                  
                          b = Data(Time=ds.Time)
                          b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information')
                      
                      
                     try:                                                  
                          b = Data(NbFiles=ds.NbFiles)
                          b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information') 
                      
                      
                      try:                                                  
                          b = Data(Progress=ds.Progress)
                          b.save()
                                            
                  except NameError:
                      print('not possible to know this information')    
                  except AttributeError:    
                      print('not possible to know this information')
                                         
                      
                    
                      
                      
               except pydicom.errors.InvalidDicomError:
                       print('not possible to know this information')
                       
