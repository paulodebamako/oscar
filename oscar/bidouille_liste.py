from random import*
liste_f = []

for colonne in range(15):
    liste = list()
    for ligne in range(15):
        liste.append(0)
        
    liste_f.append(liste)

print(liste_f)
##print('espace')
##liste_f[0][0] = 5
##print(liste_f)
        




##while len(liste_pos)!= total_agent:    
##    x= randint(0,24)
##    y= randint(0,24)
##    pos=[x,y]
##    liste_pos.append(pos)
##    if pos in liste_pos==True:
##        liste_pos.pop()
    

##for i in range(total_agent):                # coordonnees sur la grille
##        x = randint(0,24)
##        y = randint(0,24)
##        pos = [x,y]
##        liste_pos.append(pos)
##        if pos in liste_pos == True:
##            liste_pos.pop()
x= 1
y=1
for colonne in range(0,6):
    for ligne in range(0,6):
        try :
            liste_f[x-colonne][y-ligne] = 1   #creer en 1er une longue ligne sur la ligne de pos puis fait les autres ligne de part et d'autre
            liste_f[x+colonne][y-ligne] = 1
            liste_f[x-colonne][y+ligne] = 1
            liste_f[x+colonne][y+ligne] = 1
        except:
            pass
print('espace') 
print(liste_f)
