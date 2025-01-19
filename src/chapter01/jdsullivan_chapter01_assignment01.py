#!/usr/bin/env python3
""" JDSullivan's code solution to Chapter 1 - Assignment 1.

Public repo: https://github.com/JosephDSullivan/COP2373/blob/main/src/chapter01/jdsullivan_chapter01_assignment01.py

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


#   Constant(s)
MAX_TICKET_PER_TRANS: int = 4
"""int: Maximum number of tickets purchasable per transaction."""

MAX_TICKET_AVAIL: int = 20
"""int: Maximum number of tickets available for entire sale."""

#   Variable(s)
ticket_remain: int = MAX_TICKET_AVAIL
"""int: Number of tickets remaining for entire sale. """


def main():
    pass


#

def validate_sale(sale_count: str) -> int:
    """
    Validate the number of tickets as a positive integer and less than or
        equal to constant MAX_TICKET_PER_TRANS and global ticket_remain.

    >>> validate_sale("5")
    5

    >>> validate_sale("7.0")
    7

    >>> validate_sale("3.9")
    -1

    >>> validate_sale("a")
    -1

    Args:
        sale_count (str): The number of tickets the user wants to buy.

    Returns:
        int: Returns the number of sales if valid. Returns -1 otherwise.

    TODO:
        Reimplement this function to take any type of input, including float,
        int, lists, dictionaries, tuples, etc. and output the same type with
        every data point tested if valid.

    """
    #   Constant(s)
    #   Variable(s)
    global ticket_remain
    #   Verify sale count is numeric by casting to float.
    try:
        sale_count_float = float(sale_count)
    except:
        return -1
    #   Verify sale count is integer by casting and comparing to float. Note:
    #   this feels janky - I hope there is another way. This will allow a
    #   whole number written as a decimal to be valid.
    sale_count_int = int(sale_count_float)
    if sale_count_int != sale_count_float:
        return -1
    #   Verify sale count is not negative and less than or equal to both
    #   MAX_TICKET_PER_TRANS and ticket_remain.
    if sale_count_int < 0 or sale_count_int > MAX_TICKET_PER_TRANS or \
            sale_count_int > ticket_remain:
        return -1
    #   Sale count is valid. Return it.
    return sale_count_int


#


if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
#
