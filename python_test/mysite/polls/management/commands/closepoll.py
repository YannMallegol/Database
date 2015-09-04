import os, pydicom
from django.core.management.base import BaseCommand
from polls.models import Question, Choice, Key





class Command(BaseCommand):
    help = 'that does my stuff'


    def handle(self, *args, **options):

       for dossier, sous_dossiers, fichiers in os.walk('/neuro/users/yann.mallegol/Documents/internship/chris-db/python_test/dicoms'):
           for fichier in fichiers:
               fullpath = os.path.join(dossier, fichier)

               print(fullpath)
               try:
                  ds = pydicom.read_file(fullpath)
                  try:
                      ma_question = Question.objects.create(question_text=ds.StationName,
                                                            question_text1=ds.ManufacturerModelName,
                                                            question_text2=ds.MagneticFieldStrength,
                                                            question_text3=ds.Modality)
                      #question= Question()
                      #question= Question( question_text=ds.StationName,question_text1=ds.ManufacturerModelName,question_text2=ds.MagneticFieldStrength,question_text3=ds.Modality)
                  #question.question_texte=ds.StationName
                  except NameError:
                      question.question_text='undefined'
                  except NameError:
                      question.question_text1= 'undefined'
                  except NameError:
                      question.question_text2='undefined'
                  except NameError:
                      question.question_text3 = 'undefined'

                  ma_question.save()
                  #import pdb; pdb.set_trace()

                  try:
                      choice=Choice.objects.create(choice_text = ds.PatientID, question=ma_question)
                      choice.save()
#                      choice=Choice()
#                      choice = Choice.objects.get(pk=1)
#                      exemple= Question.objects.get(question_text=ds.StationName)
#                      choice.question = exemple
#                      choice.save()


                  except NameError:
                      choice.choice_text='undefined'

                  #choice.save()



                  key=Key()
                  key=Key.objects.create(sport = 'coucou', key_test= ma_question)



               except pydicom.errors.InvalidDicomError:
                       print('not possible to know this information')
