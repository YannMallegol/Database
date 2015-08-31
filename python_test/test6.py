import pydicom, os

for element in os.listdir('/neuro/users/yann.mallegol/Documents/internship/chris-db/python_test'):
   if element.endswith('.dcm'):
     print(element)
     ds = pydicom.read_file(element)
     #print(ds.PatientName)
     name = ds.PatientName
     print name


   else:
     print("'%s' n'est pas un fichier dicom" % element)
