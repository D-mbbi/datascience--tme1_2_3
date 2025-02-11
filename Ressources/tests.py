from tme1 import *
from time_calculator import *

etus=lectureEtu("PrefEtu.txt")
spes=lectureSpe("PrefSpe.txt")

affectations_etu,iter_etu=GaleShapleyEtu(etus,spes[0],spes[1].copy())
print("\n##### Affectation obtenue (Parcours: {Etudiants}) avec le coté étudiants: \n",affectations_etu,"\n")

affectations_prc,iter_prc=GaleShapleyPrc(etus,spes[0],spes[1].copy())
print("\n##### Affectation obtenue (Parcours: {Etudiants}) avec le coté parcours: \n", GaleShapleyPrc(etus,spes[0],spes[1].copy()),"\n")

paires_instables_etu = verifier_stabilite(affectations_etu, etus, spes[0])
paires_instables_prc = verifier_stabilite(affectations_prc, etus, spes[0])

print("Paires instables étudiants: ", paires_instables_etu)
print("Paires instables parcours: ", paires_instables_prc)

nb_etudiants = [_ for _ in range(200,2001,200)]
iterations_GS_etu = []
iterations_GS_prc = []
temps_moyen_GS_etu,iterations_GS_etu= time_calculator_etu()
temps_moyen_GS_prc,iterations_GS_prc = time_calculator_prc()



plt.figure(figsize=(10, 6))
plt.plot(nb_etudiants,temps_moyen_GS_etu,label="Gale Shapley coté étudiants",color='b')
plt.plot(nb_etudiants,temps_moyen_GS_prc,label="Gale Shapley coté parcours",color='r')
plt.legend()
plt.title("Temps d'exécution de l'algorithme de Gale-Shapley en fonction du nombre d'étudiants")
plt.xlabel("Nombre d'étudiants")
plt.ylabel("Temps moyen d'exécution (en s)")
plt.savefig("GaleShapleyTime.png")
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(nb_etudiants, iterations_GS_etu, label="Gale Shapley côté étudiants", color='b')
plt.plot(nb_etudiants, iterations_GS_prc, label="Gale Shapley côté parcours", color='r')
plt.legend()
plt.title("Temps d'exécution de l'algorithme de Gale-Shapley en fonction du nombre d'itérations")
plt.xlabel("Nombre d'étudiants")
plt.ylabel("Nombre d'itérations")
plt.savefig("GaleShapleyIterations.png")
plt.show()