# -*- coding: utf-8 -*-
from math import *
planetSize = 6300
# in km
eyeHeight = 1.5 / 1000
# in m
distance = 0

print('Distance to Horizon')

def calc_distance():
    distance = sqrt((2 * planetSize + eyeHeight) * eyeHeight) * 1.06
    return distance

def print_params():
    if calc_distance() < 1.0:
        distanceString = "Horizon is {0:,.1f} m away".format(calc_distance() * 1000)
    else:
        distanceString = "Horizon is {0:,.1f} km away".format(calc_distance())
    if planetSize < 1.0:
        print('Radius of the planet: {0:,.2f} m'.format(planetSize * 1000))
    else:
        print('Radius of the planet: {0:,.2f} km'.format(planetSize))

    print('          Eye height: {0:,.2f} m'.format(eyeHeight * 1000))
    print(distanceString)

print_params()

while type != "0":
   print("[0]uit [1]Size of Planet [2]Eye Height")
   type=input("Enter Number [0]-[2] > ")
   if type == "1":
      rI=input("Enter radius of the planet in km >> ")
      planetSize = float(rI)
      print_params()
   elif type == "2":
      eI=input("Enter height of eye/camera in m >> ")
      eyeHeight = float(eI) / 1000
      print_params()

print("Quit")