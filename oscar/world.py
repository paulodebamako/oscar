from random import *
from entite import *

def creation_grille():
    """creation de la grille WORLD"""
    
    global world
    world=[]
    
    for colonne in range(25):
        w = list()
        for colonne in range(25):
            w.append(0)
        world.append(w)   
    #print(world)
        
    for colonne in world:
        for ligne in world:
            case = Case()       #creation objet case pour chaque case de la grille
        
#-----------------------------------------------------

def creation_field(cat_agent,location):
    """ creation de la zone ou s'applique le field de chaque agent """
    assert isinstance(cat_agent),'Erreur cat_agent doit être un int '
    assert isinstance(location),'Erreur location doit être une liste '

    




#-----------------------------------------------------

def creer_agent(cat_agent,location):
    """ creation d'un agent (pour naissance sûr, peut-etre pour tous ?)"""
    assert isinstance(cat_agent, str),'Erreur cat_agent doit être un str '
            
#-----------------------------------------------------

def supprimer_agent(objet_agent):
    """ supprime un agent de la grille (pour mort) """

#-----------------------------------------------------

            
def creation_agent(nb_Ah, nb_Ac, nb_V, nb_M):
    """creation des agents et de leur place sur la grille"""
    assert isinstance(nb_Ah, int),'nb_Ah doit être un entier'
    assert isinstance(nb_Ac, int),'nb_Ac doit être un entier'
    assert isinstance(nb_V, int),'nb_V doit être un entier'
    assert isinstance(nb_M, int),'nb_M doit être un entier'

    total_agent = nb_Ah +nb_Ac +nb_V +nb_M      # total agent
    
    if total_agent>=600:
        print("Il y a trop d'agent dans l'environnement !")

    else:
        
        liste_pos = []

        while len(liste_pos)!= total_agent:    
            x= randint(0,24)
            y= randint(0,24)
            pos=[x,y]
            if pos in liste_pos:     #verifier qu'il n'y ait pas de doublon
                pass
                #print('DOUBLE')
            else:
                liste_pos.append(pos)
                for i in range(len(liste_pos)):     #positionner agent sur la grille + creation objet agent
                    if i<nb_Ah-1:
                        world[x][y] = 'Ah'
                        #animal_herbivore = Animal(2,2,2,5,0,'herbivore',pos, 'present',fonctioncreerfield('animal'pos) )
                    if i<nb_Ah+nb_Ac-1 and i>=nb_Ah:
                        world[x][y] = 'Ac'
                        #animal_carnivore = Animal(2,2,2,5,0,'carnivore')
                    if i<nb_Ah+nb_Ac+nb_V-1 and i>=nb_Ah+nb_Ac:
                        world[x][y] = 'V'
                        #vegetal = Vegetal(2,2,2,5,0)
                    if i<total_agent-1 and i>=nb_Ah+nb_Ac+nb_V:
                        world[x][y] = 'M'
                        #mineral = Mineral()
            
        
        
    print('nb_total agent =',total_agent)
    print('longeur liste pos =',len(liste_pos))
    print('liste pos = ',liste_pos)
    print('espace')
    print(world)

    #debugueur avec agent
##    valeur_Ah = 0
##    valeur_Ac = 0
##    valeur_V = 0
##    valeur_M = 0
##    for colonne in range(25):
##        for ligne in range(25):
##            if world[colonne][ligne] == 'Ah':
##                valeur_Ah = valeur_Ah +1
##            if world[colonne][ligne] == 'Ac':
##                valeur_Ac = valeur_Ac +1
##            if world[colonne][ligne] == 'M':
##                valeur_M = valeur_M +1
##            if world[colonne][ligne] == 'V':
##                valeur_V = valeur_V +1
##    print('nb Ah_grille = ',valeur_Ah)
##    print('nb Ac_grille = ',valeur_Ac)
##    print('nb V_grille = ',valeur_V)
##    print('nb M_grille = ',valeur_M)
##    total_agent_grille = valeur_Ac + valeur_Ah + valeur_M + valeur_V
##    print('nb_agent_grille',total_agent_grille)
  
    #debugueur sans agent
    


creation_grille()
creation_agent(15,4,10,8)
