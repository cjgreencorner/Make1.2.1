#!/usr/bin/env python
##########################################
#           Leeftijd berekenen           #
##########################################
#IMPORTS

#AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Supporter"

#CONFIGURATIONS

#EXTRA


#FUNCTIONS


def test(a, b): #maak een functie aan die 'a - b' doet.
    return a - b


def lol(a, b, c): #maak een functie aan die 'a - b + c' doet.
    return a - b + c

def  main():
    KEUZE = float(input("Leeftijd in jaren: ")) #laat de gebruiker zijn leeftijd invullen
    JAAR = 2020 #sneller dan 2x '2020' typen
    print("je bent geboren in het jaar:", test(JAAR, KEUZE)) #het jaar - de keuze die je gemaakt hebt
    print("Je bent 50 in het jaar", lol(JAAR, KEUZE, 50)) #2020 - de keuze + 50

    
if __name__ == '__main__':
    main()