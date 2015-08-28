
import pydicom, os

for element in os.listdir('/neuro/users/yann.mallegol/Documents/internship/chris-db/python_test'):
   if element.endswith('.dcm'):


     ################# for the Patient table ################
     print(element)
     ds = pydicom.read_file(element)
     try:
       patient_name=ds.PatientName
       print(patient_name)
     except NameError:
         print('not possible to know this information')
     except AttributeError:
         print('not possible to know this information')

     try:
       gender=ds.PatientSex
       print(gender)
     except NameError:
         print('not possible to know this information')
     except AttributeError:
         print('not possible to know this information')

     try:
       dob=ds.PatientBirthDate
       print(dob)
     except NameError:
         print('not possible to know this information')
     except AttributeError:
         print('not possible to know this information')

     try:
       age=ds.PatientAge
       print(age)
     except NameError:
         print('not possible to know this information')
     except AttributeError:
         print('not possible to know this information')

      #try:
        #pathology=ds.
        #print()
      #except NameError:
         #print('not possible to know this information')

      #try:
        #mrn=ds.
        #print()
      #except NameError:
         #print('not possible to know this information')







        ################# for the Study table #################

     try:
       study_name=ds.StudyID
       print(study_name)
     except NameError:
         print('not possible to know this information')
     except AttributeError:
         print('not possible to know this information')

      #try:
        #series_name=ds.
      #except NameError:
        # print('not possible to know this information')

     try:
       protocol_name=ds.ProtocolName
       print(protocol_name)
     except NameError:
          print('not possible to know this information')
     except AttributeError:
         print('not possible to know this information')

     try:
       station_name=ds.StationName
       print(station_name)
     except NameError:
         print('not possible to know this information')
     except AttributeError:
         print('not possible to know this information')

     try:
       manufacturer_name=ds.Manufacturer
       print(manufacturer_name)
     except NameError:
          print('not possible to know this information')
     except AttributeError:
          print('not possible to know this information')

     try:
       body_part_name=ds.BodyPartExamined
       print(body_part_name)
     except NameError:
         print('not possible to know this information')
     except AttributeError:
         print('not possible to know this information')

     try:
       slice_thickness=ds.SliceThickness
       print(slice_thickness)
     except NameError:
         print('not possible to know this information')
     except AttributeError:
         print('not possible to know this information')

     try:
       echo_time=ds.EchoTime
       print(echo_time)
     except NameError:
         print('not possible to know this information')
     except AttributeError:
         print('not possible to know this information')

     try:
       magnetic_field_strenght=ds.MagneticFieldStrength
       print(magnetic_field_strenght)
     except NameError:
         print('not possible to know this information')
     except AttributeError:
         print('not possible to know this information')

     try:
       inversion_time=ds.InversionTime
       print(inversion_time)
     except NameError:
         print('not possible to know this information')
     except AttributeError:
         print('not possible to know this information')



          ########## Series table ##########

     #try:
        #series_name=ds.
        #print(series_name)
     #except NameError:
      #    print('not possible to know this information')


          ########## Data table ##########

     try:
       inversion_time=ds.InversionTime
       print(inversion_time)
     except NameError:
         print('not possible to know this information')
     except AttributeError:
         print('not possible to know this information')
