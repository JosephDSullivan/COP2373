#!/usr/bin/env python3
""" This program is designed to pre-sell a limited number of cinema tickets.

Author
Joseph D. Sullivan <JSulli40@Student.SCF.edu>

Date
January 24, 2025

Chapter
01

Assignment
01

Repository
https://github.com/JosephDSullivan/COP2373/blob/main/src/chapter01/jdsullivan_chapter01_assignment01.py


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

#   Variable(s)


def main() -> None:
    """
    Entry function for when code is invoked directly.

    Args:


    Returns:
        None
    """
    #   Run a sale of 20 total tickets with a maximum of 4 tickets per
    #   transaction.
    get_sale(20, 4)


def get_sale(total_ticket_avail: int,
             max_per_trans: int
             ) -> None:
    """
    Get transactions, each buying tickets, repeatedly until all tickets are
        sold.

    Args:
        total_ticket_avail (int): Total tickets available for this sale.
        max_per_trans (int): Maximum number of tickets that can be sold in a
            single transaction.

    Returns:
        None

    """
    #   Tickets remaining for this sale.
    ticket_remain = total_ticket_avail
    #   Sale identifier.
    sale_id = 1
    #   Initial text to show user at start of sale.
    msg_init = f"Welcome to the SCF Cinema Pre-Sale!\n"
    msg_init += f"Total ticket available:  {ticket_remain}\n"

    #   Show initial text for sale.
    print(msg_init)
    #   Loop until no tickets remain.
    while ticket_remain > 0:
        #   Get transaction with the maximum ticket allowed as tickets
        #   remaining or maximum per transaction, whichever is lowest.
        ticket_sold = get_trans(min(ticket_remain, max_per_trans))
        #   Calculate tickets remaining after this sale.
        ticket_remain -= ticket_sold
        #   Notify user of sale.
        msg_sale = (f"\tTickets sold:  "
                    f"{ticket_sold:>{len(str(total_ticket_avail))}} , "
                    f"\tTickets remaining:  "
                    f"{ticket_remain:>{len(str(total_ticket_avail))}}")
        print(msg_sale)
        #   Iterate sale identifier.
        sale_id += 1


    #   Notify user at end of sale.
    msg_final = f"\nThe sale has concluded.\n"
    msg_final += f"Transaction count:  {sale_id - 1}\n"
    print(msg_final)


def get_trans(max_per_trans: int
              ) -> int:
    """
    Get transaction input from the user and validate it.

    Args:
        max_per_trans (int): Maximum number per transaction.

    Returns:
        int: Validated transaction.
    """
    #   Message text used to prompt user for transaction.
    msg = (f"How many tickets would you like to purchase (maximum of "
           f"{max_per_trans})? \t")
    #   Boolean to store if input is valid.
    is_trans_valid = False

    #   Loop until transaction is valid.
    while not is_trans_valid:
        #   Get transaction from user input.
        input_trans = input(msg)
        #   Validate the input.
        is_trans_valid = validate_trans(input_trans, max_per_trans)

    #   Return transaction.
    return int(input_trans)


def validate_trans(trans: str,
                   max_per_trans: int,
                   show_warning: bool = True
                   ) -> bool:
    """
    Validate the provided transaction. It should be a nonnegative integer and
        less than or equal to max_per_trans.

    Args:
        trans (str): The transaction to validate.
        max_per_trans (int): Maximum number per transaction.
        show_warning (bool, optional): If True, show warnings when validation
            fails. Defaults to True.

    Returns:
        bool: True if the transaction is valid, False otherwise.

    """
    #   Attempt to convert transaction to integer.
    try:
        trans_int = int(trans)
    #   Validation has failed.
    except ValueError:
        if show_warning:
            msg = (f"\tWARNING:\tUnable to convert string \"{trans}\" to an "
                   f"integer.")
            print(msg)
        return False
    #   If transaction is negative, validation has failed.
    if trans_int < 0:
        if show_warning:
            msg = f"\tWARNING:\t{trans_int} is not a positive integer."
            print(msg)
        return False
    #   If transaction is larger than the maximum per transaction, validation
    #   has failed.
    if trans_int > max_per_trans:
        if show_warning:
            msg = (f"\tWARNING:\t{trans_int} is larger than the maximum "
                   f"allowed per transaction ({max_per_trans}).")
            print(msg)
        return False
    #   Validation has succeeded.
    return True


if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
