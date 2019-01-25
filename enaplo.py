#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import codecs
import sys

def line():
    print("")

def fline():
    print("#" * 80)

subjects = (
    "Matek",
    "Irodalom",
    "Magyar",
    "Környezet",
    "Testnevelés",
)
line()
fline()
t = len(subjects)               # The number of subjects
################################################################################
# Read how many lines in the file
f_lines = len(codecs.open('grades.txt', 'r', 'UTF-8').readlines( ))
################################################################################
# Check the grades.txt line numbers
if t != f_lines:
    print("A grades.txt-ben az adatok nem jók!")
    print("Tantárgyak száma:", t)
    print("A grades.txt-ne lévő sorok száma:", f_lines)
    print("Javítsd ki a TXT fájlt és indítsd újra a programot.")
    print("Viszlát.")
    sys.exit()
else:
    pass
################################################################################
# Read file and write to grades variable. Line by line
with codecs.open('grades.txt', 'r', 'UTF-8') as g:
    grades = []
    for i in g:
        grades.append(i)

################################################################################
# Convert the grades strings to integer
#   --  All  --
z = 0
for z in range(0, t):
    len_matek = len(grades[z])
    j_matek = len_matek // 2  # The real numbers of subject
    matek = grades[z]
    smatek = 0
    for y in range(0, len_matek, 2):
        smatek = smatek + int(matek[y])         # Sum of subject grades
    a_matek = smatek/j_matek                    # subject average calculation
    line()
    print(" A", subjects[z], "átlagod: %.2f"% a_matek)
    line()
    fline()


