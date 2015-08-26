from path import path

for f in path('.').walkfiles('*.dcm'):
   print f
