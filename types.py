#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import array as arr
from math import pi

# int, string, list, tuple, dictionary

#---------------------------------------------------------
print("")
print("*"*80)
print("Numer:")

szam1 = 10
szam2 = 20
szam3 = 3.1415
szam4 = 3e10

print("szam1: ", szam1, szam2, szam3, szam4)
print(type(szam1))
print(type(szam3))
print(type(szam4))

#---------------------------------------------------------
print("")
print("*"*80)
print("String:")

szoveg1 = 'Milan'
szoveg2 = "Ildiko"
szoveg3 = "Zsolti"

print("szoveg1: ", szoveg1)
print(type(szoveg1))

#---------------------------------------------------------
print("")
print("*"*80)
print("Tuple:")

tup1 = (1, 2, 3, 4, 5, 6)
tup2 = (123, 456, 789)
tup3 = ('Milan', 'Ildiko', 10, 40)

print(tup1)
print(tup2[-1])
print(tup3)
print(tup3[0], tup3[2])
print("Type of tup3[0]: ",type(tup3[0]),"\nType of tup3[2]: ",type(tup3[2]))

#---------------------------------------------------------
print("")
print("*"*80)
print("Dictionari:")

dict1 = {'Name': 'Milan', 'Age': 10, 'School': 'Pattantyus'}

print("Name: ", dict1["Name"])
print("Age: ", dict1["Age"])
print("School: ", dict1["School"])

dict1['Class'] = "Fourth"

print("Class: ", dict1["Class"])
print(dict1)

#---------------------------------------------------------
print("")
print("*"*80)
print("List:")

list1 = ['apple', 'orange', 'banana', 'pineapple']
list2 = [1,2,3,4,5]
list3 = [1,2,'apple','orange']

print(list1)
print(list2)
print(list3)
print("Type of list1[0]: ", type(list1[0]))
print("Type of list2[0]: ", type(list2[0]))
print("Type of list3[0]: ", type(list3[0]))
print("Type of list3[2]: ", type(list3[2]))

print("")
for i in list1:
    print(i)

print("")
for i in list2:
    print(i)

print("")
for i in list3:
    print(i)

#---------------------------------------------------------
print("")
print("*"*80)
print("Range:")

range1 = range(5)
range2 = range(5, 10)
range3 = range(0, 12, 2)

print("range1: ", range1)
print("range2: ", range2)
print("range3: ", range3)

for i in range1:
    print(i)

print("")
for i in range2:
    print(i)

print("")
for i in range3:
    print(i)

#---------------------------------------------------------
print("")
print("*"*80)
print("Array:")

array1 = arr.array('d', [1, 3.2, 35, pi])

print("")
print (array1)
print("")

print("array1[0]: ", array1[0])
print("type of array1[0]: ", type(array1[0]))

print("")
print("array1[1]: ", array1[1])
print("type of array1[1]: ", type(array1[1]))

print("")
print("array1[2]: ", array1[2])
print("type of array1[2]: ", type(array1[2]))

print("")
print("array1[3]: ", array1[3])
print("type of array1[3]: ", type(array1[3]))

print("")
print("The value of PI from array1: %.5f"% array1[3])

print("")
print("*"*80)