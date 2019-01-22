#!/usr/bin/env python3.7
# -*- coding: UTF-8 -

# A lemeztábla sulyát kiszámolja.
# Készítette: Pető Zsolt
# Dátum: 2019

hossz = {'1':2000, '2':2500, '3':3000} # Dict 1
szel = {'1':1000, '2':1250, '3':1500}  # Dict 2

s = 7.85
z = 5

# Tábla méret kiválasztás
while True:
    try:
        i = int(input("Válassz lemez méretet! [1. 2000*1000] [2. 2500*1250] [3. 3000*1500]: "))
        if i < 1 or i > 3:
           i = 0
        else:
            pass
        y = z/i
        break
    except ZeroDivisionError:
        print("Kérlek 1-3-ig válassz!")
    except ValueError:
        print("Ez nem egy szám, vagy nem egész érték lett megadva!")

ii = str(i)
hs = hossz[ii]*szel[ii]

# Vastagság
w = False
vx = 0
while w != True or vx < 1:
    v = input("Milyen vastag a lemez? Pl.: 3, 2: ")
    vx = float(v)
    w = v.isdigit()

vv = int(v)

# A lemez súllya.
e = (hs*vv*s)/10**6

hosszu = str(hossz[ii])
szeles = str(szel[ii])
vastag = str(vv)

print("-"*80)
ered = ' '.join(['A lemez súllya: %.2f' %e, 'kg.'])
tabl = ' '.join([hosszu, 'mm *', szeles, 'mm *', vastag, 'mm'])
print(tabl.center(80))
print(ered.center(80))
print("-"*80)

