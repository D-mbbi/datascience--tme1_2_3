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


etus=lectureEtu("PrefEtu.txt")
spes=lectureSpe("PrefSpe.txt")

"""

"""

def GaleShapleyEtu(etu_pref : list,spe_pref : list, capacites : list):
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
    
    while etu_libres:
        etu=etu_libres.pop()    # index de l'etudiant courant
        preferences_etu_courant=etu_pref[etu]
        married = False         # variable indiquant si l'etudiant a ete affecté à l'issue de l'algo
        for prc in (preferences_etu_courant):          # prc = parcours courant, on va chercher le premier parcours parmi les preférés de l'etudiant,
                                                       # à qui il n'a pas fait de propositions
            if prc not in propositions[etu]:
                capacites[prc]=int(capacites[prc])      # conversion en int pour éviter les érreurs
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
                        if spe_pref[prc].index(etu_aff)>spe_pref[prc].index(etu_moins_pref):
                            etu_moins_pref = etu_aff
                    
                    ## On les compare ##
                    if(spe_pref[prc].index(etu_moins_pref)>spe_pref[prc].index(etu)):
                        etu_libres.add(etu_moins_pref)
                        affectations[prc].add(etu)
                        married = True
                        break
                    ## Si le parcours refuse l'éudiant, il faut réstaurer l'affectation du moins pref à cause du .pop() en l.73 ##
                    affectations[prc].add(etu_moins_pref)

                propositions[etu].add(prc) # maj des propositions faites par l'étudiant
                break

        if not married: etu_libres.add(etu) # si l'étudiant n'a pas obtenu d'affectation, il retourne dans la file d'attente

    return affectations

print("\n\nAffectation obtenue (Parcours: {Etudiants}): ", GaleShapleyEtu(etus,spes[0],spes[1]))