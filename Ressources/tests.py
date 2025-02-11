from tme1 import *
from time_calculator import *

etus=lectureEtu("PrefEtu.txt")
spes=lectureSpe("PrefSpe.txt")

affectations_etu=GaleShapleyEtu(etus,spes[0],spes[1].copy())
print("\n##### Affectation obtenue (Parcours: {Etudiants}) avec le coté étudiants: \n",affectations_etu,"\n")

affectations_prc=GaleShapleyPrc(etus,spes[0],spes[1].copy())
print("\n##### Affectation obtenue (Parcours: {Etudiants}) avec le coté parcours: \n", GaleShapleyPrc(etus,spes[0],spes[1].copy()),"\n")

paires_instables_etu = verifier_stabilite(affectations_etu, etus, spes[0])
paires_instables_prc = verifier_stabilite(affectations_prc, etus, spes[0])

print("Paires instables étudiants: ", paires_instables_etu)
print("Paires instables parcours: ", paires_instables_prc)

print(time_calculator())