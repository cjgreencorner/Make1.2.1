#!/usr/bin/env python
"""
Random woorden lijst
"""
# IMPORTS

# AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Supporter"

# CONFIGURATIONS


# EXTRA


# FUNCTIONS
def main():
    LIJST =  ["banaan", "appel", "aardbei", "komkommer"] #de variabele 'LIJST' word aangemaakt
    print(LIJST) #hier word de lijst getoond aan de gebruiker
    VRAAG = input("Geef 2 woorden(WOORD1 WOORD2): ").split()
    #hier word de gebruiker gevraagd 2 woorden te geven die aan de lijst worden toegevoegd
    LIJST.extend(VRAAG) #hier word de lijst aangevuld met de 2 extra woorden die de gebruiker gegeven heeft
    print(LIJST) #hier word de lijst opnieuw weergegeven inclusief de 2 nieuwe woorden


if __name__ == '__main__':
    main()
