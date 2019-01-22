#!/usr/local/bin/python3.7
# -*- coding: UTF-8 -*-

# Ebböl lehet function-t csinálni.

i = 0
y = 5
ss = ":("
sh = ":)"

while True:
    try:
        i = int(input("Értékeld a munkám [1-10] közötti számmal: "))
        if i < 0 or i > 10:
           i = 0
        else:
           pass
        z = y/i
        break
    except ValueError:
        print ("Ez nem egy szám, vagy nem egész érték lett megadva!")
    except ZeroDivisionError:
        print ("Kérlek 1-10-ig válassz!")

if i < 5:
   print("Ezt a számot választottad: ", i, ss)
else:
   print("Ezt a számot választottad: ", i, sh)
