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
    res1=[]
    for i in range(0,len(contenu)):
        contenu[i]=contenu[i].split()
    res2=contenu[1][1:]
    for i in range(2,len(contenu)):
        res1.append(contenu[i][2:])
    return (res1,res2)


etus=lectureEtu("PrefEtu.txt")
spes=lectureSpe("PrefSpe.txt")

"""

"""

def GaleShapleyEtu(etu_pref,spe_pref):
    spe_pref,capacites=spe_pref
    etu_libres=set()
    parcours_libres=set()

    for i in range(len(etu_pref)):
        etu_libres.add(i)
    for i in range(len(spe_pref)):
        parcours_libres.add(i)
    
    choix_parcours=dict()
    for i in range(len(spe_pref)):
        choix_parcours[i]=spe_pref[i]
    affectations=dict()

    while etu_libres:
        etu=etu_libres.pop()
        courant=etu_pref[etu]
        for j in range(len(courant)):
            capacites[j]=int(capacites[j])
            if capacites[j]!=0:
                affectations[j]=[etu]
                capacites[j]-=1
            elif capacites[j]==0: 
                for i in range(len(affectations[j])):
                    if choix_parcours[j].index(etu)<choix_parcours[j].index(affectations[j][i]):
                        etu_libres.add(i)
                        affectations[j][i]=etu
                        break
            else:
                etu_libres.add(etu)

    return choix_parcours

print(GaleShapleyEtu(etus,spes))
