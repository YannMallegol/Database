import pydicom, os

for element in os.listdir('/neuro/users/yann.mallegol/Documents/internship/chris-db/python_test'):
	 if element.endswith('.dcm'):
		 print("'%s' est un fichier dicom" % element)
		 ds = pydicom.read_file(element)
		 print(ds.PatientName)
		 try:
				print(ds.SeriesDescription)
		 except NameError:
			print('not possible to know this information')
		 print(ds.SeriesNumber)
	
		 
	 else:
		 print("'%s' n'est pas un fichier dicom" % element)
