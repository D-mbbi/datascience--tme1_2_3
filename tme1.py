def lectureEtu(s): 
    monFichier = open(s, "r") 
    contenu = monFichier.readlines()
    monFichier.close() 
    res=[]
    for i in range(0,len(contenu)):
        contenu[i]=contenu[i].split()
    for i in range(1,len(contenu)):
        res.append(contenu[i][2:])
    return res


def lectureSpe(s):
    monFichier = open(s, "r") 
    contenu = monFichier.readlines()
    monFichier.close()
    res1=[]         #   matrice des parcours avec leurs préférences
    for i in range(0,len(contenu)):
        contenu[i]=contenu[i].split()
    res2=contenu[1][1:] #   liste des capacités des parcours
    for i in range(2,len(contenu)):
        res1.append(contenu[i][2:])
    return (res1,res2)




def GaleShapleyEtu(etu_pref : list,spe_pref : list, capacites : list):
    iterations = 0
    for i in range(len(etu_pref)):                          # Conversion en int du contenu des matrices de preferences
        for j in range(len(etu_pref[i])):
            etu_pref[i][j] = int(etu_pref[i][j])
    for i in range(len(spe_pref)):
        for j in range(len(spe_pref[i])):
            spe_pref[i][j] = int(spe_pref[i][j])
    
    
    etu_libres=set()    #set qui contiendra les ID des étudiants libres
    for i in range(len(etu_pref)):
        etu_libres.add(i)

    affectations=dict()     #dictionnaire des affectations parcours -> {étudiants} qui sera retourné
    for i in range(len(spe_pref)):
        affectations[i] = set()
    
    propositions=dict()     #utilisé pour voir les propositions qu'ont fait les étudiants
    for i in range(len(etu_pref)):
        propositions[i] = set()
    
    prc_prefs=dict()      #dictionnaire pour stocker l'ordre de préférence des étudiants pour chaque parcours
    for prc in range(len(spe_pref)):
        prc_prefs[prc]={etu: pref for pref, etu in enumerate(spe_pref[prc])}


    while etu_libres:
        etu=etu_libres.pop()    # index de l'etudiant courant
        preferences_etu_courant=etu_pref[etu]
        married = False         # variable indiquant si l'etudiant a ete affecté à l'issue de l'algo
        for prc in (preferences_etu_courant):          # prc = parcours courant, on va chercher le premier parcours parmi les preférés de l'etudiant,
                                                       # à qui il n'a pas fait de propositions 
            iterations += 1
            if prc not in propositions[etu]:
                capacites[prc]=int(capacites[prc])      # conversion en int pour éviter les erreurs
                if capacites[prc] > 0:              # s'il reste de la place dans le parcours on ajoute l'étudiant
                    affectations[prc].add(etu)
                    capacites[prc]-=1
                    married = True
                    
                    break
                else:                                               #sinon si le parcours préfère cet étudiant plutot que l'étudiant qu'il préfère le moins
                                                                    #parmi ceux qui lui sont affectés, ce dernier est remplacé :'(
                    ## Recherche du moins préféré ##
                    etu_moins_pref = affectations[prc].pop()     
                    for etu_aff in affectations[prc]:
                        if prc_prefs[prc][etu_aff]>prc_prefs[prc][etu_moins_pref]:  
                            etu_moins_pref = etu_aff
                    
                    ## On les compare ##
                    if(prc_prefs[prc][etu_moins_pref]>prc_prefs[prc][etu]):
                        etu_libres.add(etu_moins_pref)
                        affectations[prc].add(etu)
                        married = True
                        break
                    ## Si le parcours refuse l'éudiant, il faut réstaurer l'affectation du moins pref à cause du .pop() en l.73 ##
                    affectations[prc].add(etu_moins_pref)

                propositions[etu].add(prc) # maj des propositions faites par l'étudiant
                break

        if not married: etu_libres.add(etu) # si l'étudiant n'a pas obtenu d'affectation, il retourne dans la file d'attente

    return affectations,iterations



def GaleShapleyPrc(etu_pref : list,spe_pref : list, capacites : list):
    iterations = 0
    for i in range(len(etu_pref)):          # Conversion en int du contenu des matrices de preferences
        for j in range(len(etu_pref[i])):
            etu_pref[i][j] = int(etu_pref[i][j])
    for i in range(len(spe_pref)):
        for j in range(len(spe_pref[i])):
            spe_pref[i][j] = int(spe_pref[i][j])
    
    
    spe_libres=set()    #set qui contiendra les ID des parcours libres
    for i in range(len(spe_pref)):
        spe_libres.add(i)
    
    etu_libres=set()    #set qui contiendra les ID des étudiants libres
    for i in range(len(etu_pref)):
        etu_libres.add(i)
    
    affectations=dict()     #dictionnaire des affectations parcours -> {étudiants} qui sera retourné
    for i in range(len(spe_pref)):
        affectations[i] = set()
    
    propositions=dict()     #utilisé pour voir les propositions qu'ont fait les parcours
    for i in range(len(spe_pref)):
        propositions[i] = set()
    
    while spe_libres:
        prc=spe_libres.pop()
        preferences_spe_courant=spe_pref[prc]
        married=False 
        capacites[prc]=int(capacites[prc])

        while capacites[prc]>0:
            

            for etu in (preferences_spe_courant):
                iterations += 1
                if etu not in propositions[prc]:
                    propositions[prc].add(etu) # maj des propositions faites par les parcours
                    if etu in etu_libres:
                        affectations[prc].add(etu)
                        capacites[prc]-=1
                        etu_libres.remove(etu)
                        break
                    
                    else:
                        #Recherche du parcours dans lequel se situe l'étudiant etu
                        prc_aff = -1
                        for aff in affectations.items():
                            if etu in aff[1]: 
                                prc_aff = aff[0]
                                break
                        if(etu_pref[etu].index(prc) < etu_pref[etu].index(prc_aff)):
                            affectations[prc_aff].remove(etu)
                            capacites[prc_aff] += 1
                            spe_libres.add(prc_aff)
                            affectations[prc].add(etu)
                            capacites[prc] -= 1
                            break

                    
    return affectations,iterations



def verifier_stabilite(affectations, etu_pref, spe_pref):
    paires_instables = []    
    for spe, etus in affectations.items():
        for etu in etus:
            for meilleur_spe in etu_pref[etu]:
                if meilleur_spe == spe:
                    break  #l'étudiant est satisfait
                
                else:
                    etus_du_parcours = affectations[meilleur_spe]
                    
                    for etu_moins_pref in etus_du_parcours:
                        if spe_pref[meilleur_spe].index(etu) < spe_pref[meilleur_spe].index(etu_moins_pref):
                            paires_instables.append((etu, meilleur_spe))
                            break
    
    return paires_instables

def generer_fichier_lp(pref_etu,capacites, k, output_file="affectation.lp"):
    nb_etudiants=len(pref_etu)
    nb_specialites=len(capacites)

    with open(output_file, "w") as f:
        f.write("Maximize\n")
        f.write("obj: 0\n")  #pas d'objectif particulier, on cherche juste une faisabilité
    
        f.write("Subject To\n")
        
        #Contrainte 1 : chaque étudiant est affecté à exactement une spécialité parmi ses k premiers choix
        for i in range(nb_etudiants):
            k_choix = pref_etu[i][:k]  # Les k premiers choix
            f.write(f" c_Etu_{i}: " + " + ".join([f"x_{i}_{j}" for j in k_choix]) + " = 1\n")

        #Contrainte 2 : ne pas dépasser la capacité des spécialités
        for j in range(nb_specialites):
            f.write(f" c_Spe_{j}: " + " + ".join([f"x_{i}_{j}" for i in range(nb_etudiants) if j in pref_etu[i][:k]]) + f" <= {capacites[j]}\n")

        #variables binaires
        f.write("Binary\n")
        for i in range(nb_etudiants):
            for j in pref_etu[i][:k]:
                f.write(f"x_{i}_{j}\n")

        f.write("End\n")
    print(f"Fichier {output_file} généré.")

    

def generer_lp_max_utilite(pref_etu, pref_spe, capacites, filename="max_utilite.lp"):
    nb_etudiants = len(pref_etu)
    nb_parcours = len(pref_spe[0])

    with open(filename, "w") as f:
        f.write("Maximize\n")
        f.write(" obj: " + " + ".join(
            [f"{(nb_parcours - pref_etu[i][j])} x_{i}_{j}" for i in range(nb_etudiants) for j in range(nb_parcours)]
        ) + "\n")

        f.write("\nSubject To\n")
        
        # Chaque étudiant doit être affecté à un seul parcours
        for i in range(nb_etudiants):
            f.write(f" c1_{i}: " + " + ".join([f"x_{i}_{j}" for j in range(nb_parcours)]) + " = 1\n")

        # Respect des capacités des parcours
        for j in range(nb_parcours):
            f.write(f" c2_{j}: " + " + ".join([f"x_{i}_{j}" for i in range(nb_etudiants)]) + f" <= {capacites[j]}\n")

        f.write("\nBinary\n")
        for i in range(nb_etudiants):
            for j in range(nb_parcours):
                f.write(f" x_{i}_{j}\n")

        f.write("\nEnd\n")

    print(f"Fichier {filename} généré.")

def generer_lp_max_k(pref_etu, pref_spe,capacites,k, filename="max_utilite_k.lp"):
    nb_etudiants = len(pref_etu)
    nb_parcours = len(pref_spe[0]) 

    with open(filename, "w") as f:
        f.write("Maximize\n")
        f.write(" obj: " + " + ".join(
            [f"{(nb_parcours - pref_etu[i][j])} x_{i}_{j}" for i in range(nb_etudiants) for j in range(nb_parcours)
             if pref_etu[i].index(j) < k]  # On garde uniquement les k* premiers choix
        ) + "\n")

        f.write("\nSubject To\n")
        
        # Chaque étudiant doit être affecté à un seul parcours
        for i in range(nb_etudiants):
            f.write(f" c1_{i}: " + " + ".join([f"x_{i}_{j}" for j in range(nb_parcours) if pref_etu[i].index(j) < k]) + " = 1\n")

        # Respect des capacités des parcours
        for j in range(nb_parcours):
            f.write(f" c2_{j}: " + " + ".join([f"x_{i}_{j}" for i in range(nb_etudiants)]) + f" <= {capacites[j]}\n")

        f.write("\nBinary\n")
        for i in range(nb_etudiants):
            for j in range(nb_parcours):
                if pref_etu[i].index(j) < k:
                    f.write(f" x_{i}_{j}\n")

        f.write("\nEnd\n")

    print(f"Fichier {filename} généré.")



