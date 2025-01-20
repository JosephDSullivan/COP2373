#!/usr/bin/env python3
#   Copyright 2025 JSulli40@Student.SCF.edu
import sys

#   COP2373 - Chapter  - Question .
#
#   tbd.
#

#   Import(s)
import sympy
from chapter01 import jdsullivan_chapter01_assignment01 as c01a01

#   Constant(s)
TXT_IF_PASS: str = "✔"
"""str: Text to display if test passes."""
TXT_IF_FAIL: str = "❌"
"""str: Text to display if test fails."""
#   Variable(s)
#   None

def main():
    validate_sale_test()
#

def validate_sale_test():
    sale_count = "2"
    output_expected = 2
    output_actual = c01a01.validate_sale(sale_count=sale_count)
    output_text = f"validate_sale({"\"" + str(sale_count) + "\"":>7}) -> "
    output_text += f"{output_actual:>2}\t"
    if output_actual == output_expected:
        output_text += TXT_IF_PASS
    else:
        output_match = TXT_IF_FAIL
    print(output_text)

    sale_count = "3.0"
    output_expected = 3
    output_actual = c01a01.validate_sale(sale_count=sale_count)
    output_text = f"validate_sale({"\"" + str(sale_count) + "\"":>7}) -> "
    output_text += f"{output_actual:>2}\t"
    if output_actual == output_expected:
        output_text += TXT_IF_PASS
    else:
        output_match = TXT_IF_FAIL
    print(output_text)

    sale_count = "0"
    output_expected = 0
    output_actual = c01a01.validate_sale(sale_count=sale_count)
    output_text = f"validate_sale({"\"" + str(sale_count) + "\"":>7}) -> "
    output_text += f"{output_actual:>2}\t"
    if output_actual == output_expected:
        output_text += TXT_IF_PASS
    else:
        output_match = TXT_IF_FAIL
    print(output_text)

    sale_count = "-3"
    output_expected = -1
    output_actual = c01a01.validate_sale(sale_count=sale_count)
    output_text = f"validate_sale({"\"" + str(sale_count) + "\"":>7}) -> "
    output_text += f"{output_actual:>2}\t"
    if output_actual == output_expected:
        output_text += TXT_IF_PASS
    else:
        output_match = TXT_IF_FAIL
    print(output_text)

    sale_count = "2.9"
    output_expected = -1
    output_actual = c01a01.validate_sale(sale_count=sale_count)
    output_text = f"validate_sale({"\"" + str(sale_count) + "\"":>7}) -> "
    output_text += f"{output_actual:>2}\t"
    output_text += TXT_IF_PASS if output_actual == output_expected else \
        TXT_IF_FAIL
    print(output_text)

    sale_count = "a"
    output_expected = -1
    output_actual = c01a01.validate_sale(sale_count=sale_count)
    output_text = f"validate_sale({"\"" + str(sale_count) + "\"":>7}) -> "
    output_text += f"{output_actual:>2}\t"
    if output_actual == output_expected:
        output_text += TXT_IF_PASS
    else:
        output_match = TXT_IF_FAIL
    print(output_text)
#


def play_sympy():
    x = sympy.symbols("x")
    f = "sin(2*x)"

    print("f(x)       = " + str(f) + "\n")

    f_diff = sympy.diff(f, x)

    print("derivative = " + str(f_diff))

    f_integrate = sympy.integrate(f, x)

    print("integrate  = " + str(f_integrate))


#

if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
#
