#!/usr/bin/env python3
""" JDSullivan's code solution to Chapter 01 - Assignment 01.

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
import datetime as dt

#   Constant(s)

#   Variable(s)

def main():
    """
    Entry function for when code is invoked directly.

    Args:


    Returns:
        None
    """
    #   Run a sale of 20 total tickets with a maximum of 4 tickets per
    #   transaction.
    sales = get_sale(20,4)
    #   Display a table of all sale data.
    print(f"{'Sale ID':^8}\t"
          f"{'Sale Date / Time':^30}\t"
          f"{'Initial':^8}\t"
          f"{'Sold':^5}\t"
          f"{'Remain':^7}\t")
    for sale in sales:
        msg_sale = (f"{sale['sale_id']:>8}\t"
                    f"{sale['sale_dttm']:>30}\t"
                    f"{sale['ticket_init']:>8}\t"
                    f"{sale['ticket_sold']:>5}\t"
                    f"{sale['ticket_remain']:>7}")
        print(msg_sale)

def get_sale(total_ticket_avail: int,
             max_per_trans: int
             ) -> tuple[dict[int,str]]:
    """

    Args:
        total_ticket_avail:
        max_per_trans:

    Returns:

    """
    #   Variable(s)
    #   Tickets remaining for this sale.
    ticket_remain = total_ticket_avail
    #   Identifier for each sale, starting with 1.
    sale_id = 1
    #   All sale data.
    sale_data = []
    #   Initial text to show user at start of sale.
    msg_init = f"Welcome to the SCF Cinema Pre-Sale!\n"
    msg_init += f"Total ticket available:  {ticket_remain}\n"

    #   Show initial text for sale.
    print(msg_init)
    #   Loop until no tickets remain.
    while ticket_remain > 0:
        #   Store sale datetime and initial ticket count.
        sale_dttm = dt.datetime.now()
        ticket_init = ticket_remain
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
        #   Store sale sale.
        sale_data.append({
            "sale_id": sale_id,
            "sale_dttm": sale_dttm.strftime("%Y-%m-%d %H:%M:%S.%f %Z%z"),
            "ticket_init": ticket_init,
            "ticket_sold": ticket_sold,
            "ticket_remain": ticket_remain,
        })
        #   Iterate sale ID.
        sale_id += 1

    #   Notify user at end of sale.
    msg_final = f"\nThe sale has concluded.\n"
    msg_final += f"Total transactions:  {sale_id}\n"
    print(msg_final)
    #   Return sale data cast as tuple.
    return tuple(sale_data)


def get_trans(max_per_trans: int
              ) -> int:
    """
    Get transaction input from the user and validate it.

    Args:
        max_per_trans (int): Maximum number per transaction.

    Returns:
        int: Validated transaction count
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