#!/usr/bin/env python3
#   Copyright 2025 JSulli40@Student.SCF.edu

#   COP2373 - Chapter  - Question .
#
#   tbd.
#

#   Import(s)
import sympy as sp

#   Variable(s)
#   None

def main():
    print('\n')

    x = sp.symbols('x')
    f = sp.sin(x)

    print('f(x)       = ' + str(f) + '\n')

    f_diff = sp.diff(f, x)

    print('derivative = ' + str(f_diff))

    f_integrate = sp.integrate(f, x)

    print('integrate = ' + str(f_integrate))
#

if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
#