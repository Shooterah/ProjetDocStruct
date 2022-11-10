from os import listdir
from os.path import isfile, join


fichiers = [f for f in listdir("Questions") if isfile(join("Questions", f))]
print(fichiers)
