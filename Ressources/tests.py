from tme1 import *
from time_calculator import *

etus=lectureEtu("PrefEtu.txt") 
spes=lectureSpe("PrefSpe.txt")

affectations_etu,iter_etu=GaleShapleyEtu(etus,spes[0],spes[1].copy())
print("\n##### Affectation obtenue (Parcours: {Etudiants}) avec le coté étudiants: \n",affectations_etu,"\n") #Affectations sur l'exemple PrefEtu.txt 

affectations_prc,iter_prc=GaleShapleyPrc(etus,spes[0],spes[1].copy())
print("\n##### Affectation obtenue (Parcours: {Etudiants}) avec le coté parcours: \n",affectations_prc) #Affectations sur l'exemple PrefEtu.txt

paires_instables_etu = verifier_stabilite(affectations_etu, etus, spes[0]) #Vérification de la stabilité des affectations
paires_instables_prc = verifier_stabilite(affectations_prc, etus, spes[0])

print("Paires instables étudiants: ", paires_instables_etu)
print("Paires instables parcours: ", paires_instables_prc)

# Comparaison des temps d'exécution et du nombre d'itérations de l'algorithme de Gale-Shapley en fonction du nombre d'étudiants

nb_etudiants = [_ for _ in range(200,2001,200)]
iterations_GS_etu = []
iterations_GS_prc = []
temps_moyen_GS_etu,iterations_GS_etu= time_calculator_etu()
temps_moyen_GS_prc,iterations_GS_prc = time_calculator_prc()
"""
plt.figure(figsize=(10, 6))
plt.plot(nb_etudiants,temps_moyen_GS_etu,label="Gale Shapley coté étudiants",color='b')
plt.plot(nb_etudiants,temps_moyen_GS_prc,label="Gale Shapley coté parcours",color='r')
plt.legend()
plt.title("Temps d'exécution de l'algorithme de Gale-Shapley en fonction du nombre d'étudiants")
plt.xlabel("Nombre d'étudiants")
plt.ylabel("Temps moyen d'exécution (en s)")
plt.savefig("GaleShapleyEtuTime.png")
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(nb_etudiants, iterations_GS_etu, color='b')
plt.title("Nombre d'itérations de l'algorithme de Gale-Shapley côté étudiant")
plt.xlabel("Nombre d'étudiants")
plt.ylabel("Nombre d'itérations")
plt.savefig("GaleShapleyEtuIterations.png")
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(nb_etudiants, iterations_GS_prc, color='r')
plt.title("Nombre d'itérations de l'algorithme de Gale-Shapley côté parcours")
plt.xlabel("Nombre d'étudiants")
plt.ylabel("Nombre d'itérations")
plt.savefig("GaleShapleyPrcIterations.png")
plt.show()
"""
#PLNE

generer_fichier_lp(etus,spes[1], k=5)
generer_lp_max_utilite(etus, spes, spes[1])
