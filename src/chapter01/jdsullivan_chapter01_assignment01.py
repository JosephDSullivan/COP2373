#!/usr/bin/env python3
""" Code solution to Chapter 1 - Assignment 1.

Functions:



Write an application to pre-sell a limited number of cinema tickets. Each
buyer can buy up to 4 tickets. No more than 20 tickets can be sold total.
Prompt the user for the desired number of tickets and then display the number
of remaining tickets after their purchase. Repeat until all tickets have been
sold. Then display the total number of buyers.

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

    Args:
        sale_count (str): The number of tickets the user wants to buy.

    Returns:
        int: Returns the number of sales indicated by parameter sale_count
            if valid. Returns zero otherwise.
    """
    #   Constant(s)

    #   Variable(s)
    global ticket_remain
    #   Verify sale_count is numeric. Convert sale_count to int. On any
    #   error, return zero.
    try:
        sale_count_float = float(sale_count)
    except:
        return 0


#


if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
#
