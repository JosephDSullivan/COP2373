#!/usr/bin/env python3
#   Copyright 2025 JSulli40@Student.SCF.edu
import sys

#   COP2373 - Chapter  - Question .
#
#   tbd.
#

#   Import(s)
import sympy as sp

#   Variable(s)
#   None

def  main():
    print_docstrings()
#

def print_docstrings():
    a = float(60.0)
    b = int(a)
    print(a)
    print(b)
    print(a == b)
#


def play_sympy():
    x = sp.symbols("x")
    f = "sin(2*x)"

    print("f(x)       = " + str(f) + "\n")

    f_diff = sp.diff(f, x)

    print("derivative = " + str(f_diff))

    f_integrate = sp.integrate(f, x)

    print("integrate  = " + str(f_integrate))
#

if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
#