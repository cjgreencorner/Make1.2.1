#!/usr/bin/env python
"""
Stopwatch
"""
# IMPORTS

# AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Supporter"

# CONFIGURATIONS
import time #hier importeer ik de library 'time'

# EXTRA


# FUNCTIONS
def tijd(sec): #hier maak ik de functie tijd aan
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60 #hier geef ik aan hoelang 'seconden, minuten en uren' zijn.
  print("Tijd voorbijgegaan = {0} uur, {1} minuten, {2} seconden".format(int(hours),int(mins),sec)) #dit is het bericht dat de gebruiker krijft met de exacte tijd die voorbij gegaan is.
input("Druk op Enter om te starten") #hier laat ik de gebruiker het moment kiezen wqnneer het programma start met tellen
start_tijd = time.time() #hier begint de tijd me tellen
input("Druk op Enter om te stoppen") #hier laat je de gebruiker kiezen wanneer hij de tijd stopt
stop_tijd = time.time() #de tijd stopt met tellen
klok = stop_tijd - start_tijd #hier word het verschil tussen de twee tijden berekend
tijd(klok)

if __name__ == '__tijd__':
    tijd(sec)
