import tme1
import random
import time
from statistics import mean


def matrice_cE(n):
    cE = []
    for i in range(n):
       cE.append([j for j in range(9)])
       random.shuffle(cE[i])
    return cE

def matrice_cP(n):
    cP = []
    for i in range(9):
       cP.append([j for j in range(n)])
       random.shuffle(cP[i])
    return cP
def generate_integer_list_v2(n, total):
    numbers = [1] * n  # Initialiser tous les nombres à 1 (au moins 1 par case)
    total -= n  # On a déjà utilisé `n` unités
    
    for _ in range(total):
        numbers[random.randint(0, n - 1)] += 1  # Ajouter 1 à une case aléatoire

    return numbers

def time_calculator():
    print("Chargement...")
    temps_par_n = []
    for i in range(200,2001,200):
        cE = matrice_cE(i)
        cP = matrice_cP(i)
        capacites = generate_integer_list_v2(9,i)
        temps=[]
        for k in range(10):
            start = time.time()
            tme1.GaleShapleyEtu(cE,cP,capacites.copy())
            end = time.time()
            
            temps.append(end-start)
        temps_par_n.append(mean(temps))
    return temps_par_n



