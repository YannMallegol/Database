import os, pydicom
from django.core.management.base import BaseCommand, CommandError
from polls.models import Question, Choice
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
                  print(ds.PatientName)

                  try:
                      print(ds.SeriesDescription)
                      description = ds.SeriesDescription
                      question_text=description
                      print (question_text)
                      database_connexion = sqlite.connect('polls.sqlite')
                      cursor = database_connexion.cursor()
                      cursor.execute("insert into Question values (null,?,?)", (question_text))
                      database_connexion.commit()
                      cursor.close()
                      #q=Question(question_text="description")
                      #q=save()
                      #c.execute("test", (description))
                      #c.close()
                      
                  except NameError:
                      print('not possible to know this information')
                  try:
                      print(ds.SeriesNumber)
                  except NameError:
                      print('not possible to know this information')

               except pydicom.errors.InvalidDicomError:
                       print('not possible to know this information')
