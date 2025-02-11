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

nb_etudiants = [_ for _ in range(200,2001,200)]
temps_moyen_GS_etu = time_calculator_etu()
plt.plot(nb_etudiants,temps_moyen_GS_etu)
plt.title("Gale Shapley coté étudiants")
plt.xlabel("Nombre d'étudiants")
plt.ylabel("Temps moyen d'éxécution (en s)")
plt.show()

temps_moyen_GS_prc = time_calculator_prc()
plt.plot(nb_etudiants,temps_moyen_GS_prc)
plt.title("Gale Shapley coté parcours")
plt.xlabel("Nombre d'étudiants")
plt.ylabel("Temps moyen d'éxécution (en s)")
plt.show()
