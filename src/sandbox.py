#!/usr/bin/env python3
""" JDSullivan's code solution to Chapter 01 - Assignment 01.

Public repo: https://github.com/JosephDSullivan/COP2373/blob/main/src/sandbox.py

Problem description:

"""


#   Import(s)
import sympy

#   Constant(s)

#   Variable(s)

def main():
    play_sympy()


#
def play_sympy():
    fx = "sin(2*x)"
    x = sympy.symbols("x")

    f_diff_1 = sympy.diff(fx, x)
    f_diff_2 = sympy.diff(f_diff_1, x)
    f_integrate = sympy.integrate(fx, x)
    print()
    print(f"{'f(x)':<25}={fx}")
    print(f"{"1st derivative": <25}={f_diff_1}")
    print(f"{"2nd derivative": <25}={f_diff_2}")
    print(f"{"Integral": <25}={f_integrate}")


#

if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
#
