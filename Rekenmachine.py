#!/usr/bin/env python
"""
Simpel rekenmachine
"""
# IMPORTS

# AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Supporter"

# CONFIGURATIONS


# EXTRA


# FUNCTIONS
def maal(a, b): #hier maak ik de maal functie aan
    return a * b


def main():
    num1 = float(input("Voer eerste cijfer in: ")) #hier word de gebruiker gevraagd het eerste cijfer te geven
    num2 = float(input("Voer tweede cijfer in: ")) #hier word de gebruiker gevraagd het tweede cijfer te geven
    print(num1, "*", num2, "=", maal(num1, num2)) #hier word de uitkomst geprint


if __name__ == '__main__':
    main()
