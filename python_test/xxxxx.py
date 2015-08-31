import os, pydicom

for dossier, sous_dossiers, fichiers in os.walk('/neuro/users/chris/data'):
  for fichier in fichiers:
      fullpath = os.path.join(dossier, fichier)
      print(fullpath)
      try:
        ds = pydicom.read_file(fullpath)
        print(ds.PatientName)
        try:
             print(ds.SeriesDescription)
        except NameError:
           print('not possible to know this information')
        try:
          print(ds.SeriesNumber)
        except NameError:
          print('not possible to know this information')

      except pydicom.errors.InvalidDicomError:
       print('not possible to know this information')
