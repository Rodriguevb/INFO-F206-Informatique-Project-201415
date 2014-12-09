import sys
import random


def createDNA (n):
	"""
	Crée un brin d'ADN sans aucune répétition en tandem.
	"""
    sigma = []
    alphabetgenetique = ["A","C","G","T"]

    while len(sigma) < n: # Tant qu'on obtient pas la longueur de brin d'ADN voulu, la boucle continue à tourner.
        print (sigma)
        sigma . append (alphabetgenetique [ random . randint(0,3) ]) # Ajoute à la fin du code génétique la lettre de l'aplphabet génétique correspondant à la valeur d'un entier aléatoire entre 0 et 3..
        print (sigma)
        p = 1
        arret = False
        
        # La boucle vérifie s'il y a une répétition en tandem dans le code génétique du brin.
        while 2*p <= len (sigma) and arret == False: # tant que le nombre de derniers éléments du brin est inférieur ou égal à la longeur du brin et que arrêt vaut false, la boulce continue à tourner
            if verificationTandem(sigma[-2*p:]) == True : # sigma[-2*p:] prends les derniers éléments de la liste, la fonction renvoie vraie s'il y a une répétition.
                
                #la boucle supprime l'élément qui était répété dans le code génétique du brin.
                for i in range (p):
                    print ("L'élément supprimé est: ", sigma.pop()) # sigma.pop() supprime le dernier élément de la liste
                    arret = True
                    
            else:
                p += 1
        
    return sigma



def verificationTandem( liste ):
    """
	Renvoie si la première moitié de la liste et la deuxième moitié de la liste sont égaux.
	"""
    a = (liste[:len(liste)//2] == liste [len(liste)//2:]) 
    return a




if len(sys.argv) >= 2:
    print( "Brin d'ADN:", createDNA( int( sys.argv[1] ) ) )
else:
    print( "Il manque un argument pour la longueur souhaitée." )





























