import os, pydicom
from django.core.management.base import BaseCommand
from polls.models import Question, Choice, Key, MR_Params, US_Params, CT_Params, Review





class Command(BaseCommand):
    help = 'that does my stuff'


    def handle(self, *args, **options):

       for dossier, sous_dossiers, fichiers in os.walk('/neuro/users/yann.mallegol/Documents/internship/chris-db/python_test/dicoms'):
           for fichier in fichiers:
               fullpath = os.path.join(dossier, fichier)
               if fichier.endswith('.dcm'):
                print(fullpath)
                ds = pydicom.read_file(fullpath)



                ################# Patient table ###################

                try:
                  PatientId=ds.PatientId
                except NameError:
                  PatientId = 'undefined'
                except AttributeError:
                  PatientId = 'undefined'


                try:
                  PatientName=ds.PatientName
                except NameError:
                  PatientName = 'undefined'
                except AttributeError:
                  PatientName = 'undefined'

                try:
                  PatientAge=ds.PatientAge
                except NameError:
                  PatientAge = 'undefined'
                except AttributeError:
                  PatientAge = 'undefined'  

                try:
                  PatientSex=ds.PatientSex
                except NameError:
                  PatientSex = 'undefined'
                except AttributeError:
                  PatientSex = 'undefined'  

                try:
                  PatientBirthDate=ds.PatientBirthDate
                except NameError:
                  PatientBirthDate = 'undefined'
                except AttributeError:
                  PatientBirthDate = 'undefined'  

                try:
                  PatientBirthTime=ds.PatientBirthTime
                except NameError:
                  PatientBirthTime = 'undefined'
                except AttributeError:
                  PatientBirthTime = 'undefined'  


                
                b1=Question(PatientId=PatientId, PatientAge=PatientAge, PatientSex=PatientSex,
                 PatientBirthDate=PatientBirthDate, PatientBirthTime=PatientBirthTime)
                b1.save()


                
                ################## Study table ####################


                try:
                  StudyDescription=ds.StudyDescription
                except NameError:
                  StudyDescription = 'undefined'
                except AttributeError:
                  StudyDescription = 'undefined'

                try:
                  StationName=ds.StationName
                except NameError:
                  StationName = 'undefined'
                except AttributeError:
                  StationName = 'undefined'
                  
                try:
                  ManufacturerModelName=ds.ManufacturerModelName
                except NameError:
                  ManufacturerModelName = 'undefined'
                except AttributeError:
                  ManufacturerModelName = 'undefined'   

                try:
                  StudyInstanceUID=ds.StudyInstanceUID
                except NameError:
                  StudyInstanceUID = 'undefined'
                except AttributeError:
                  StudyInstanceUID = 'undefined' 

                try:
                  Pathology=ds.Pathology
                except NameError:
                  Pathology = 'undefined'
                except AttributeError:
                  Pathology = 'undefined' 
                  
                try:
                  StudyDate=ds.StudyDate
                except NameError:
                  StudyDate = 'undefined'
                except AttributeError:
                  StudyDate = 'undefined' 

                try:
                  StudyTime=ds.StudyTime
                except NameError:
                  StudyTime = 'undefined'
                except AttributeError:
                  StudyTime = 'undefined'


                try:
                  AccessionNumber=ds.AccessionNumber
                except NameError:
                  AccessionNumber = 'undefined'
                except AttributeError:
                  AccessionNumber = 'undefined'

                try:
                  InstitutionName=ds.InstitutionName
                except NameError:
                  InstitutionName = 'undefined'
                except AttributeError:
                  InstitutionName = 'undefined'


                try:
                  ReferringPhysicianName=ds.ReferringPhysicianName
                except NameError:
                  ReferringPhysicianName = 'undefined'
                except AttributeError:
                  ReferringPhysicianName = 'undefined'

                try:
                  PerformingPhysicianName=ds.PerformingPhysicianName
                except NameError:
                  PerformingPhysicianName = 'undefined'
                except AttributeError:
                  PerformingPhysicianName = 'undefined'  


                try:
                  ModalitiesInStudy=ds.ModalitiesInStudy
                except NameError:
                  ModalitiesInStudy = 'undefined'
                except AttributeError:
                  ModalitiesInStudy = 'undefined'
                  
                try:
                  MagneticFieldStrength=ds.MagneticFieldStrength
                except NameError:
                  MagneticFieldStrength = 0
                except AttributeError:
                  MagneticFieldStrength = 0




                b2=Choice(StudyDescription=StudyDescription,StationName=StationName,ManufacturerModelName=ManufacturerModelName,
                  StudyInstanceUID=StudyInstanceUID,Pathology=Pathology,StudyDate=StudyDate,
                  StudyTime=StudyTime,AccessionNumber=AccessionNumber,InstitutionName=InstitutionName,
                  ReferringPhysicianName=ReferringPhysicianName,ModalitiesInStudy=ModalitiesInStudy,
                  MagneticFieldStrength=MagneticFieldStrength,patient=b1)
                b2.save()
                      


                ####################### Series table ######################


                try:
                  SeriesNumber=ds.SeriesNumber
                except NameError:
                  SeriesNumber = 'undefined'
                except AttributeError:
                  SeriesNumber = 'undefined'

                try:
                  SeriesInstanceUID=ds.SeriesInstanceUID
                except NameError:
                  SeriesInstanceUID = 'undefined'
                except AttributeError:
                  SeriesInstanceUID = 'undefined' 
                  
                try:
                  ProtocolName=ds.ProtocolName
                except NameError:
                  ProtocolName = 'undefined'
                except AttributeError:
                  ProtocolName = 'undefined'

                try:
                  Modality=ds.Modality
                except NameError:
                  Modality = 'undefined'
                except AttributeError:
                  Modality = 'undefined'
                  
                try:
                  AccessionNumber=ds.AccessionNumber
                except NameError:
                  AccessionNumber = 'undefined'
                except AttributeError:
                  AccessionNumber = 'undefined'    


                try:
                  SeriesDescription=ds.SeriesDescription
                except NameError:
                  SeriesDescription = 'undefined'
                except AttributeError:
                  SeriesDescription = 'undefined'   

                try:
                  SeriesTime=ds.SeriesTime
                except NameError:
                  SeriesTime = 'undefined'
                except AttributeError:
                  SeriesTime = 'undefined'
                  
                try:
                  ContrastAgent=ds.ContrastAgent
                except NameError:
                  ContrastAgent = 'undefined'
                except AttributeError:
                  ContrastAgent = 'undefined'
                  

                try:
                  ScanningSequence=ds.ScanningSequence
                except NameError:
                  ScanningSequence = 'undefined'
                except AttributeError:
                  ScanningSequence = 'undefined'

                try:
                  BodyPartExaminated=ds.BodyPartExaminated
                except NameError:
                  BodyPartExaminated = 'undefined'
                except AttributeError:
                  BodyPartExaminated = 'undefined'  
                  
                try:
                  AcquisitionNumber=ds.AcquisitionNumber
                except NameError:
                  AcquisitionNumber = 'undefined'
                except AttributeError:
                  AcquisitionNumber = 'undefined' 
                  

                b3=Key(SeriesNumber=SeriesNumber,SeriesInstanceUID=SeriesInstanceUID,ProtocolName=ProtocolName,Modality=Modality,AccessionNumber=AccessionNumber,
                            SeriesDescription=SeriesDescription,SeriesTime=SeriesTime,ContrastAgent=ContrastAgent,ScanningSequence=ScanningSequence,
                            BodyPartExaminated=BodyPartExaminated,AcquisitionNumber=AcquisitionNumber,study=b2)   
                b3.save()





              ############ MR_Params table ##############


                try:
                  PixelSpacing=ds.PixelSpacing
                except NameError:
                  PixelSpacing = 'undefined'
                except AttributeError:
                  PixelSpacing = 'undefined'

                try:
                  SliceThickness=ds.SliceThickness
                except NameError:
                  SliceThickness = 'undefined'
                except AttributeError:
                  SliceThickness = 'undefined'


                try:
                  EchoTime=ds.EchoTime
                except NameError:
                  EchoTime = 'undefined'
                except AttributeError:
                  EchoTime = 'undefined'

                try:
                  EchoNumbers=ds.EchoNumbers
                except NameError:
                  EchoNumbers = 'undefined'
                except AttributeError:
                  EchoNumbers = 'undefined'  


                try:
                  InversionTime=ds.InversionTime
                except NameError:
                  InversionTime = 'undefined'
                except AttributeError:
                  InversionTime = 'undefined' 
                  
                try:
                  RepetitionTime=ds.RepetitionTime
                except NameError:
                  RepetitionTime = 'undefined'
                except AttributeError:
                  RepetitionTime = 'undefined'
                  



                b4=MR_Params(PixelSpacing=PixelSpacing,SliceThickness=SliceThickness,EchoTime=EchoTime,EchoNumbers=EchoNumbers,
                  InversionTime=InversionTime,RepetitionTime=RepetitionTime,
                  modality_params= b3)
                  
                b4.save()

                ############# US_Params ###############

                try:
                  Name=ds.Name
                except NameError:
                  Name = 'undefined'
                except AttributeError:
                  Name = 'undefined'

                b5=US_Params(Name=Name,modality_params=b3)
                b5.save()


                ################ CT_Params ####################


                try:
                  Name=ds.Name
                except NameError:
                  Name = 'undefined'
                except AttributeError:
                  Name = 'undefined'

                b6=CT_Params(Name=Name,modality_params=b3)
                b6.save()

                ##################### Review  ################

                try:
                  Name=ds.Name
                except NameError:
                  Name = 'undefined'
                except AttributeError:
                  Name = 'undefined'

                try:
                  Comment=ds.Comment
                except NameError:
                  Comment = 'undefined'
                except AttributeError:
                  Comment = 'undefined'
                  
                try:
                  Rating=ds.Rating
                except NameError:
                  Rating = 0
                except AttributeError:
                  Rating = 0

                b7=Review(Name=Name,Comment=Comment,Rating=Rating, study=b2,serie=b3)
                b7.save()


             
                  








               else:
                print("'%s' n'est pas un fichier dicom" % fichier)




