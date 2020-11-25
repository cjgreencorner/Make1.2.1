#!/usr/bin/env python
"""

"""
# IMPORTS
# from gpiozero.pins.pigpio import PiGPIOFactory
import os

# CONFIGURATIONS
# IP = PiGPIOFactory(host='joel')


# AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Supporter"


# FUNCTIONS
ANTWOORD = "tomaat"
LIJST = "appel, banaan, appelsien, aardbei, mango, watermeloen, ONZICHTBAAR"
LA = "appel, banaan, appelsien, aardbei, mango, watermeloen, tomaat" #Dit is het volledige antwoord
print("") #Laat vrije ruimtes tussen alles
print(LIJST)
print("")
print("Je hebt 5 pogingen!")
print("")
guess = input("Raad het laatste woord in de lijst! ")


# poging 1
if guess == ANTWOORD: #Als je het antwoord van de eerste keer juist hebt
    print("")
    print(LA)
    print("")
    print("Je hebt vals gespeeld! :(")
    print("")
    input("Druk op Enter om af te sluiten!")

else: #Als je een fout antwoord geeft
    os.system('cls')
    print("")
    print("Het antwoord is helaas niet", guess, ":(")
    print("")
    print("Nog 4 pogingen resterend!")
    print("")
    print(LIJST)
    guess = input("Raad het laatste woord in de lijst! ")


    # poging 2
    if guess == ANTWOORD:
        print("")
        print(LA)
        print("")
        print("Goed gedaan! Gelukt na 2 pogingen!")
        print("")
        input("Druk op Enter om af te sluiten!")

    else:
        os.system('cls')
        print("")
        print("Het antwoord is helaas niet", guess, ":(")
        print("")
        print("Nog 3 pogingen resterend!")
        print("")
        print(LIJST)
        guess = input("Wat is het laatste woord in de lijst? ")



        # poging 3
        if guess == ANTWOORD:
            print("")
            print(LA)
            print("")
            print("Goed gedaan! Gelukt na 3 pogingen!")
            print("")
            input("Druk op Enter om af te sluiten!")

        else:
            os.system('cls')
            print("")
            print("Het antwoord is helaas niet", guess, ":(")
            print("")
            print("Nog 2 pogingen resterend!")
            print("")
            print(LIJST)
            guess = input("Wat is het laatste woord in de lijst? ")


# poging 4
            if guess == ANTWOORD:
                print("")
                print(LA)
                print("")
                print("Goed gedaan! Gelukt na 4 pogingen!")
                print("")
                input("Druk op Enter om af te sluiten!")

            else:
                os.system('cls')
                print("")
                print("Het antwoord is helaas niet", guess, ":(")
                print("")
                print("Nog 1 pogingen resterend!")
                print("")
                print(LIJST)
                guess = input("Je kan dit, ik duim voor jou! ")

# poging 5
                if guess == ANTWOORD:
                    print("")
                    print(LA)
                    print("")
                    print("Goed gedaan! Gelukt na 5 pogingen!")
                    print("")
                    input("Druk op Enter om af te sluiten!")

                else:
                    os.system('cls')
                    print("")
                    print("Het antwoord is helaas niet", guess, ":(")
                    print("")
                    print("Goed gespeeld! Het antwoord was", ANTWOORD)
                    print("")
                    print("Tomaat is echt fruit! Zoek maar op!")
                    print("")
                    print(LA)
                    print("")
                    input("Druk op Enter om af te sluiten!")