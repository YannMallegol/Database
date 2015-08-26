import pydicom, os

for element in os.listdir('/neuro/users/yann.mallegol/Documents/internship/chris-db/python_test'):
     if element.endswith('.dcm'):
         print("'%s' est un fichier dicom" % element)
     else:
         print("'%s' n'est pas un fichier dicom" % element)
