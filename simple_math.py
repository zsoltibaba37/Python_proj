#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from inpcheck import *

import datetime
import time
import os

def main():
    while True:
        z = "Simple math program"
        today = str(datetime.date.today())
        ops = ["+", "-", "*", "/"]

        print("#"*80)
        print(z.center(80))
        print(today.center(80))
        print("#"*80)


        num1 = integer_check("Enter first number: ")
        print("#"*80)


        op = "a"
        while op not in (ops):
            op = name_check("Enter operator: ")
        print("#"*80)


        num2 = integer_check("Enter second number: ")
        print("#"*80)

        if op == ops[0]:
            a = num1 + num2
            print("            ", num1, str(ops[0]), num2)
            print("The result: ", a)
        elif op == ops[1]:
            s = num1 - num2
            print("            ", num1, str(ops[1]), num2)
            print("The result: ", s)
        elif op == ops[2]:
            m = num1 * num2
            print("            ", num1, str(ops[2]), num2)
            print("The result: ", m)
        elif op == ops[3]:
            d = float(num1 / num2)
            print("            ", num1, str(ops[3]), num2)
            print("The result: ", "%.2f"% d)

        print("#"*80)
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      pass

