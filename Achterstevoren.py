#!/usr/bin/env python
"""
Een woord achterwaards maken
"""
# IMPORTS
# from gpiozero.pins.pigpio import PiGPIOFactory


# CONFIGURATIONS
# IP = PiGPIOFactory(host='joel')


# AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Supporter"


# FUNCTIONS
def main():
    string = input("Geef een willekeurig woord in: ") #De gebruiker word om een woord gevraagd
    text=len(string) #Hier word gezegd dat dit woord om de letters draait
    backwards=string[text::-1] #Hier word het woord volledig gereversed
    print(backwards) #Hier word de gereversde text geprint


if __name__ == '__main__':
    main()
