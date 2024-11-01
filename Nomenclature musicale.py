import os


chemin = "D:\\Music"
fichiers = list ()
dossiers = list (os. walk (chemin))
for dossier in dossiers:
    fichiers. extend (dossier [2])
for fichier in fichiers:
    nom = str (fichier)
    if len (nom) > 138:
        print (nom)