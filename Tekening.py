#!/usr/bin/env python
"""
Stel dat je een lijst met lijsten hebt waar elke waarde in de binnenste lijsten een tekenreeks is
"""
# IMPORTS
# from gpiozero.pins.pigpio import PiGPIOFactory


# CONFIGURATIONS
# IP = PiGPIOFactory(host='joel')


# AUTHORINFO
__author__ = "Joel Chapon"
__email__ = "joel.chapon@student.kdg.be"
__status__ = "Supporter"



grid =   [['.', '.', '.', '.', '.', '.'],
          ['.', 'O', 'O', '.', '.', '.'],
          ['O', 'O', 'O', 'O', '.', '.'],
          ['O', 'O', 'O', 'O', 'O', '.'],
          ['.', 'O', 'O', 'O', 'O', 'O'],
          ['O', 'O', 'O', 'O', 'O', '.'],
          ['O', 'O', 'O', 'O', '.', '.'],
          ['.', 'O', 'O', '.', '.', '.'],
          ['.', '.', '.', '.', '.', '.']]

# Normaal
print("")
print("Normaal:")
print("")
for i in range(6): #Van links tot het 6e vakje rechts
    for a in range(9): #Van boven tot het 9e vakje beneden
        if a < 8: #Dit zorgt er voor dat de 'returns' op de juiste plek zijn
            print(grid[a][i], end="")
        else:
            print(grid[a][i])

# Omgekeerd
print("")
print("Omgekeerd:")
print("")
for i in range(6):
    for a in range(9):
        if a < 8:
            print(grid[a][-(i+1)], end="") #Hier reverse ik eigenlijk de range waardoor het hartje op zijn kop staat
        else:
            print(grid[a][i])
