import os, pydicom

for dossier, sous_dossiers, fichiers in os.walk('/neuro/users/chris/data'):
    for fichier in fichiers:
        print(os.path.join(fichier))
