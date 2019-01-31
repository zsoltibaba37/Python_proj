#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

__author__ = "Zsolt Pető"
__license__ = "MIT"
__version__ = "0.2"

import codecs
import time
import sys
import random
import textwrap

def line():
    print("")

def fulline():
    print("#" * 80)

def range_check(a,b):
    """
    Checks your choice between two numbers.
    Usage:
    range_check(1,10)
    Return rating value.
    """
    y = 0
    while y != 1:
        try:
            i = int(input("?>: "))
            if i in range(a,b+1):
               y = 1
               pass
            else:
               print("Válassz a fenti listából!")
               y = 0
        except ValueError:
            print ("A beírt érték nem szám, vagy nem egész szám!")
            y = 0
    return i


# Hány sor van az orban.txt-ben
file_lines = len(codecs.open('orban.txt', 'r', 'UTF-8').readlines( ))

# Ellenőrzi az orban.txt fájlt. Ha üres a fájl, akkor kilép.
if file_lines == 0:
    line()
    fulline()
    print("Az orban.txt fájl üres!!!\nViszlát.")
    fulline()
    sys.exit(1)
else:
    pass

# Az csak egy lista a 'Wikidézet' évszámaival
list = [
    '1989–1993',
    '1994–1998',
    '1998–2001',
    '2002–2005',
    '2006-2018'
]

# A 'list' hossza
llist = len(list)

# Az orban.txt beolvasása az 'orban' listába.
with codecs.open('orban.txt', 'r', 'UTF-8') as o:
    orban = []                 # Létrehozza az orban nevü listát, amiben az idézetek vannak
    for i in o:
        orban.append(i)


fulline()
line()
print("Ez a kis program a magam szórakoztatására készült.")
line()
print("A lenti idézetek Orbán Viktor-tól származnak,")
print("és a 'https://hu.wikiquote.org/wiki/Orb%C3%A1n_Viktor' oldalról lettek összegyűjve.\n")
fulline()
idezet = "'A zsigerekig ható gyűlölet olyannyira központi lehet egy ember életében, hogy egész élete értelmét vesztené, ha gyűlölete tárgya megsemmisülne.'" # A társadalom fogaskerekei. Magyarázó mechanizmusok a társadalomtudományokban - Jon Elster (2001)
line()
print(textwrap.fill(idezet, 80), "\n       Jon Elster")
line()
fulline()
line()
print("Válassz a listából és utazz vissza az időben. (Pl.: 1 [Enter])")
line()
fulline()
time.sleep(1)
aa = 1
for i in list:
    print(aa,"-", i)
    aa += 1

v = range_check(1,llist)

if v == 1:
    # 1989–1993: 1-11
    a = random.randint(1, 11)
    fulline()
    line()
    print(textwrap.fill(orban[a], 80))
    line()
    fulline()
elif v == 2:
    # 1994–1998: 14-17
    b = random.randint(14, 17)
    fulline()
    line()
    print(textwrap.fill(orban[b], 80))
    line()
    fulline()
elif v == 3:
    # 1998–2001: 20-28
    c = random.randint(20, 28)
    fulline()
    line()
    print(textwrap.fill(orban[c], 80))
    line()
    fulline()
elif v == 4:
    # 2002–2005: 31-40
    d = random.randint(31, 40)
    fulline()
    line()
    print(textwrap.fill(orban[d], 80))
    line()
    fulline()
else:
    # 2006-2018: 43-86
    e = random.randint(43, 86)
    fulline()
    print(textwrap.fill(orban[e], 80))
    fulline()
