from random import*
liste_f = []

for colonne in range(15):
    liste = list()
    for ligne in range(15):
        liste.append(0)
        
    liste_f.append(liste)

#randint(0,15) 
x=7 #remettre randint après, ici 8 pour tester au centre pour voir
y=6

for i in range(y-2,y+3): #on assume que le champ a un "rayon" de 2 cases col/lignes/diagonales
    for j in range(x-2,x+3):
        if i>=0 and j>=0:
            try:
                liste_f[i][j] = 1 #si on peut assigner la valeur (case dans le champ du monde) on le fait
            except:         #sinon on passe à la prochaine case
                pass
            
        
print(liste_f)
print(x,y)


# for colonne in range(0,6):
#     for ligne in range(0,6):                #creer en 1er une longue ligne sur la ligne de pos puis fait les autres ligne de part et d'autre
#         liste_f[x-colonne][y-ligne] = 1
#         liste_f[x+colonne][y-ligne] = 1
#         liste_f[x-colonne][y+ligne] = 1
#         liste_f[x+colonne][y+ligne] = 1
#         print()
# print(liste_f)

def generer_field(agent):
    """genere le field d'un agent, cat_agent influe sur rayon du field ? """
    x=pos[0]
    y=pos[1]

    for i in range(y-2,y+3): #on assume que le champ a un "rayon" de 2 cases col/lignes/diagonales
        for j in range(x-2,x+3):
            if i>=0 and j>=0:
                try:
                    liste_f[i][j] = 1 #si on peut assigner la valeur (case dans le champ du monde) on le fait
                except:         #sinon on passe à la prochaine case
                    pass
    
    
