#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

__author__ = "Zsolt Pető"
__version__ = "0.1"

import codecs, sys

def line():
    print("")

def fline():
    print("#" * 80)

subjects = (
    "Angol nyelv",
    "Erkölcstan",
    "Ének-zene",
    "Informatika",
    "Irodalom",
    "Környezetismeret",
    "Magyar",
    "Matematika",
    "Technika",
    "Testnevelés",
    "Vizuális kultúra"
)

################################################################################
#
# The number of subjects
#
################################################################################
t = len(subjects)

################################################################################
#
# Read how many lines in the grades.txt file.
#
################################################################################
f_lines = len(codecs.open('grades.txt', 'r', 'UTF-8').readlines( ))

################################################################################
#
# Compare the grades.txt with the subjects
#
################################################################################
if t != f_lines:
    line()
    fline()
    print("A grades.txt-ben az adatok nem jók!")
    print("Tantárgyak száma:", t)
    print("A grades.txt-ne lévő sorok száma:", f_lines)
    print("Javítsd ki a TXT fájlt és indítsd újra a programot.")
    print("Viszlát.")
    line()
    fline()
    sys.exit()
else:
    pass

################################################################################
#
# Read file and write to grades variable. Line by line
#
################################################################################
with codecs.open('grades.txt', 'r', 'UTF-8') as g:
    grades = []                 # Make list from file
    for i in g:
        grades.append(i)

################################################################################
#
#   Print out averages
#
################################################################################
line()
fline()
for z in range(0, t):
    len_rating = len(grades[z]) # One line how many character contain
    r_rating = len_rating // 2  # The real numbers of ratings
    subj = grades[z]
    s_rating = 0
    for y in range(0, len_rating, 2):
        s_rating = s_rating + int(subj[y])         # Sum of subject grades
    a_rating = s_rating/r_rating                   # rating average calculation [sum of ratings / number off ratings]
    line()
    print(" A(z)", subjects[z], "átlagod: %.2f"% a_rating)

line()
fline()
