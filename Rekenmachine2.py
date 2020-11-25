#!/usr/bin/env python
##########################################
#      Simpel Rekenmachine Versie 2      #
##########################################
# IMPORTS

# AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Supporter"


# Plus
def plus(x, y): #Eerst heb ik 4 functies aangemaakt voor alle soort bewerkingen
    return x + y


# Min
def min(x, y):
    return x - y


# Maal
def maal(x, y):
    return x * y


# Gedeeld door
def delen(x, y):
    return x / y


print("1.Plus") #Hier leg ik uit wat je moet typen voor welke functie
print("2.Min")
print("3.Maal")
print("4.Delen door")


def main():
    while True:
        # Laat de gebruiker een bewerking kiezen
        keuze = input("Voer keuze in (1/2/3/4): ") #Hier maakt de gebruiker de keuze tussen min/maal/...

        # Controlleert of de gebruiker een juiste keuze gemaakt heeft
        if keuze in ('1', '2', '3', '4'): #Dit zorgt voor de flowcontrol
            num1 = float(input("Voer eerste cijfer in: ")) #De gebruiker word gevraagd het eerste cijfer in te voeren
            num2 = float(input("Voer tweede cijfer in: ")) #De gebruiker word gevraagd het tweede cijfer in te voeren

            if keuze == '1':
                print(num1, "+", num2, "=", plus(num1, num2)) #Dit gebeurd er als de gebruiker 'plus' heeft gekozen

            elif keuze == '2':
                print(num1, "-", num2, "=", min(num1, num2)) #Dit gebeurd er als de gebruiker 'min' heeft gekozen

            elif keuze == '3':
                print(num1, "*", num2, "=", maal(num1, num2)) #Dit gebeurd er als de gebruiker 'maal' heeft gekozen

            elif keuze == '4':
                print(num1, "/", num2, "=", delen(num1, num2)) #Dit gebeurd er als de gebruiker 'gedeeld door' heeft gekozen
            break
        else: #Moest de gebruiker iets anders als de 4 keuzes gemaakt hebben komt er een foutmelding
            print("Foute vermelding")


if __name__ == '__main__':
    main()
