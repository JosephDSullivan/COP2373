#!/usr/bin/env python3
""" JDSullivan's code solution to Chapter 1 - Assignment 1.

Public repo: https://github.com/JosephDSullivan/COP2373/blob/main/src/chapter01/jdsullivan_chapter01_assignment01_test.py

Problem description:
    Write an application to pre-sell a limited number of cinema tickets. Each
    buyer can buy up to 4 tickets. No more than 20 tickets can be sold total.
    Prompt the user for the desired number of tickets and then display the
    number of remaining tickets after their purchase. Repeat until all tickets
    have been sold. Then display the total number of buyers.
    Please use the following in your code:
    1. two functions - your choice how you want to design this
    2. input
    3. output
    4. accumulator
    5. if statement
    6. loop
    You must also have a technical design document (refer to the Submitting
    Assignments Module).
    Submit both your .py file and .doc/.docx file in this assignment and these
    files must also be in your repository.

"""

#   Import(s)
from src.chapter01 import jsulli40_chapter01_assignment01 as c01a01

#   Constant(s)
TXT_IF_PASS: str = "✔"
"""str: Text to display if test passes."""
TXT_IF_FAIL: str = "❌"
"""str: Text to display if test fails."""


#   Variable(s)


def main():
    test()


#

def test() -> bool:
    """
    Code to test imported module.

    Returns:
        bool: Returns True if all tests pass. Returns False otherwise.

    Todo:
        Implement a real test suite. It won't be done, but it's fun to pretend.
    """

    #   Constant(s)

    #   Variable(s)
    #   Assume all tests will pass. When any single test fails, overwrite this
    #   to False.
    all_test_pass: bool = True

    #   Test case data for validate_sale().
    test_cases = [
        ("2", 2),
        ("3.0", 3),
        ("0", 0),
        ("-3", -1),
        ("2.9", -1),
        ("a", -1),
    ]
    #   Iterate through each test case and run validate_sale(). Compare
    #   the actual output with the expected output. Report the results to
    #   the user. If any test fails, set all_test_pass to False.
    for sale_count, output_expected in test_cases:
        output_actual = c01a01.validate_sale(sale_count=sale_count)
        output_text = f"validate_sale({sale_count!r:>7}) -> "
        output_text += f"{output_actual:>2}T\t"
        if output_actual == output_expected:
            output_text += TXT_IF_PASS
        else:
            output_text += TXT_IF_PASS
            all_test_pass = False
        print(output_text)
    #   Report to the user if all tests passed (True or False).
    output_text = f"{"validate_sale(*)":>29}\t"
    output_text += f"{TXT_IF_PASS if all_test_pass else TXT_IF_FAIL}"
    print(output_text)

    #   Report to the user if all tests passed (True or False).
    output_text = f"\n{"ALL TESTS PASS?":^28}\t"
    output_text += f"{TXT_IF_PASS if all_test_pass else TXT_IF_FAIL}"
    print(output_text)


#

if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
#
