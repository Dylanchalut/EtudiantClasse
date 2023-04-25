from Etudiant import *

#Sérialiser l'objet instancié
etud = Etudiant("1852719", "Dylan", "informatique")
etud.serialiser("FichierSerialiser1.json")



#Déserialisation

etud1 = Etudiant()

etud1.deserialiser("FichierSerialiser1.json")

print(etud1)
