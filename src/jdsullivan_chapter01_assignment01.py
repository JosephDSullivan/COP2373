#!/usr/bin/env python3
#   COP2373 - Chapter 1 - Assignment 1.
#
#   Write an application to pre-sell a limited number of cinema tickets. Each
#   buyer can buy up to 4 tickets. No more than 20 tickets can be sold total.
#   Prompt the user for the desired number of tickets and then display the
#   number of remaining tickets after their purchase. Repeat until all tickets
#   have been sold. Then display the total number of buyers.
#
#   Please use the following in your code:
#   1. two functions - your choice how you want to design this
#   2. input
#   3. output
#   4. accumulator
#   5. if statement
#   6. loop
#
#   You must also have a technical design document (refer to the Submitting
#   Assignments Module).
#
#   Submit both your .py file and .doc/.docx file in this assignment and these
#   files must also be in your repository.
#

#   Import(s)
#   None

#   Variable(s)
max_ticket_per_purchase = 4
ticket_remain_count = 20

def  main():
    make_sale()
#

def make_sale():
    #   Initialize variable(s).
    global  max_ticket_per_purchase, \
            ticket_remain_count
    msg_input = "How many tickets would you like to purchase? "
    #   Query user for purchase.
    purchase_count = input(msg_input)
    #   Verify purchase_count is numeric.
    try:
        purchase_count_float = float(purchase_count)
    except ValueError:
        print(f"Error: You did not enter a number. Sale cancelled.")
        return 0
    #   Verify purchase_count is an integer.
    purchase_count = int(purchase_count)
    if purchase_count != purchase_count_float:
        print(f"Error: You did not enter a whole number. Sale cancelled.")
        return 0
    #   Verify purchase_count is positive.
    if purchase_count < 0:
        print(f"Error: You did not enter a positive number. Sale cancelled.")
        return 0
    #   Verify purchase_count is not greater than max_ticket_per_purchase.
    if  purchase_count > max_ticket_per_purchase:
        print(f"Error: You attempted to purchase more than the maximum")
        print(f"tickets per person ({max_ticket_per_purchase}). Sale ")
        print(f"cancelled.")
        return 0
    #   Verify purchase_count is not greater than ticket_remain_count.
    if  purchase_count > ticket_remain_count:
        print(f"Error: You attempted to purchase more than the total number")
        print(f"remaining tickets ({ticket_remain_count}). Sale cancelled.")
        print(f"tickets per person. Sale cancelled.")
        return 0
    #   Entry is valid. Confirm sale.
    print(f"You have successfully purchased {purchase_count} tickets.")
    return purchase_count
#

if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
#