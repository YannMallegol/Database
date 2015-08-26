import pydicom



#ds = pydicom.read_file("0076-1.2.840.113619.2.135.2025.2078900.5939.1097298450.587.dcm")
ds = pydicom.read_file("0137-1.3.12.2.1107.5.2.32.35115.2015030713550491430880042.dcm")

a = False
print(type(a))

print(ds.PatientName)
print(ds.SeriesNumber)
print(ds.PatientID)
print(ds.StudyDescription)
try:
	print(ds.SeriesDescription)
except NameError:
	print('not possible to know this information')

print(ds.InstitutionName)
try:
	print(ds.PatientBirthDate)
except NameError:
	print('not possible to know this information')

print(ds.ImageType)

q = "PatientName" in ds
print(q)

if "PatientID in ds":
	a = True
	print(a)

