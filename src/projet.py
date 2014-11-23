import random

def algoDeGrytczuk():
    # Initiliser les 4 premières lettres de l'alphabet et delta comme séquence vide
    alphabet = ["A","B","C","D"]
    delta = []

    # Répéter tant que delta est de longueur < n
    while len(delta) < 10 : # len(delta) = longueur de la liste delta
        entierAleatoire = random.randint(0,3)
        print( "____________________________________" )
        print( delta, "+", alphabet[entierAleatoire], end = "   =   " )
        delta.append( alphabet[entierAleatoire] ) # Ajoute une des 4 premières lettres de l'alphabet. Liste commence de 0 jusqu'à 3.
        print( delta )
        p = 1
        arret = False
        while 2*p <= len(delta) and not arret :
            if repetitionTandem( delta[-2*p:] ) :
                for i in range(p):
                    print( delta, end = " - " )
                    print( delta.pop(), end = "   =   " )
                    print( delta )
                arret = True
            else:
                p += 1
    return delta

def repetitionTandem( liste ):
    premiereMoitieDeListe = liste[ : len(liste)//2 ]
    deuxiemeMoitieDeListe = liste[ len(liste)//2 : ]
    egale = premiereMoitieDeListe == deuxiemeMoitieDeListe
    print( "\t|", premiereMoitieDeListe, "==", deuxiemeMoitieDeListe, "?",  egale )
    return egale
    
print( "Voici une séquence d'ADN sans répétition :", algoDeGrytczuk() )
