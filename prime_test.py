#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import inpcheck
import time


print("#"*80)
print("Meddíg keresse a prímszámokat")
b = inpcheck.integer_check()
print("#"*80)

primszamok = []
num = 1
start = time.time()
while len(primszamok) != b:
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
#                print(num, "Ez nem prím szám.")
#                print(i, "*", num // i, "=", num)
                num += 1
                break
        else:
#            print(num, "Ez prímszám. Hurrá!!!")
            primszamok.append(num)
            num += 1
    # if input number is less than
    # or equal to 1, it is not prime
    else:
#        print(num, "Ez nem prím szám.")
        num += 1

print("")
print("Ezeket a primszámokat találtam: ", sorted(primszamok))
print("Ez az első", len(primszamok), "db prímszám.")
print("")
#
x = 0
for i in primszamok:
    x += i
print("Az első", len(primszamok), "prímszám összege:", x)
print("")

if x > 1:
    # check for factors
    for i in range(2, x):
        if (x % i) == 0:
#            print(x, "Ez nem prím szám.")
#            print(i, "*", x // i, "=", x)
            break
    else:
        print(x, "Ez prímszám. Hurrá!!!")
# if input number is less than
# or equal to 1, it is not prime
else:
    pass
#    print(x, "Ez nem prím szám.")

end = time.time()
e = end - start
print("")
print("A program %.2f" % e, "másodpecíg futott.")
print("")




