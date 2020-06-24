#!/usr/bin/env/ python3
# -*- coding: UTF-8 -*-

from inpcheck import integer_check
import time


def fibo(x):
    print("")
    a, b = 1, 2
    for i in range(0, x):
        print("{}".format(a))
        c = a + b
        a = b
        b = c


y = integer_check("\nHow many numbers to calculate?: ")
tstart = time.time()
fibo(y)
tend = time.time()
trun = tend - tstart
print("\nThe calculation time(ms): {:.3f}".format(trun))

print("\nBye Bye")