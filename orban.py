#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

__author__ = "Zsolt Pető"
__license__ = "MIT"
__version__ = "0.3"

import codecs
import random
import sys
import textwrap
import time
from sys import platform
import os

# t = 10

def torles():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win32":
        os.system('cls')

def line():
    print("")

def fulline():
    print("#" * 80)

def outl():
    line()
    fulline()
    line()
    print("[CTRL-C]-re kilép a programból.".center(80))
    line()
    folyt = input("Nyomj egy [ENTER]-t a folytatáshoz".center(80))
    torles()
    return folyt

def range_check(a,b,c):
    """
    Checks your choice between two numbers.
    Usage:
    range_check(1,10,question)
    Return rating value.
    """
    y = 0
    while y != 1:
        try:
            i = int(input(c))
#            i = int(input("?>: "))
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

# Bevezető
fulline()
line()
print("Ez a kis program a magam szórakoztatására készült.")
line()
print("A lenti idézetek Orbán Viktor-tól származnak,")
print("és a 'https://hu.wikiquote.org/wiki/Orb%C3%A1n_Viktor' oldalról gyűjtöttem.\n")
fulline()
idezet = "'A zsigerekig ható gyűlölet olyannyira központi lehet egy ember életében, hogy egész élete értelmét vesztené, ha gyűlölete tárgya megsemmisülne.'" # A társadalom fogaskerekei. Magyarázó mechanizmusok a társadalomtudományokban - Jon Elster (2001)
line()
print(textwrap.fill(idezet, 80), "\n       Jon Elster")

# Loop
try:
    while True:
        fulline()
        line()

        # Lista a választáshoz
        aa = 1
        for i in list:
            print(aa, "-", i)
            aa += 1

        kerdes = "Válassz a listából és utazz vissza az időben. (Pl.: 1 [Enter]): "
        line()
        v = range_check(1, llist, kerdes)
        line()

        # Random idézet kiíratása
        if v == 1:
            # 1989–1993: 1-11
            a = random.randint(1, 11)
            fulline()
            line()
            print(textwrap.fill(orban[a], 80))
            outl()
        elif v == 2:
            # 1994–1998: 14-17
            b = random.randint(14, 17)
            fulline()
            line()
            print(textwrap.fill(orban[b], 80))
            outl()
        elif v == 3:
            # 1998–2001: 20-28
            c = random.randint(20, 28)
            fulline()
            line()
            print(textwrap.fill(orban[c], 80))
            outl()
        elif v == 4:
            # 2002–2005: 31-40
            d = random.randint(31, 40)
            fulline()
            line()
            print(textwrap.fill(orban[d], 80))
            outl()
        else:
            # 2006-2018: 43-86
            e = random.randint(43, 86)
            fulline()
            line()
            print(textwrap.fill(orban[e], 80))
            outl()

except KeyboardInterrupt:
    print("")
    sys.exit("\nViszlát\n")
