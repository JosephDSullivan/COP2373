#!/usr/bin/env python3
"""
Collect expenses from user, calculate expense totals, and display results.

Author
    Joseph D Sullivan <JSulli40@Student.SCF.edu>

Date
    February 13, 2025

Chapter
    03

Assignment
    01

Repository
    https://github.com/JosephDSullivan/COP2373/blob/main/src/chapter03/jsulli40_chapter03_assignment01.py

Problem Description
    Write a program asking the user for a list of their monthly expenses. When
    asking the user for their expenses, ask for the type of expense and the
    amount. Use the reduce method to analyze the expenses and display the
    total expense, the highest expense and the lowest expense. Label what the
    highest and lowest expense is.
    *You can use separate functions for your calculations or you can use
    lambda functions within your main function to do this.
    You must also have a technical design document (refer to the Submitting
    Assignments Module).
    Submit both your .py file and .doc/.docx file in this assignment and these
    files must also be in your repository."""

from functools import reduce
from typing import Dict, List


def main():
    """
    Entry function for when code is invoked directly. Retrieve expenses,
    calculate totals, and display results.
    """
    #   Retrieve expenses.
    expenses: List[Dict[str, float]] = get_expenses()

    #   If no expenses were entered, display a message and exit.
    if not expenses:
        print("\nNo expenses entered. Exiting program.")
        return

    #   Calculate lowest expense(s).
    lowest: List[Dict[str, float]] = get_lowest(expenses)

    #   Calculate highest expense(s).
    highest: List[Dict[str, float]] = get_highest(expenses)

    #   Calculate total expenses.
    total: float = get_total(expenses)

    #   Display results.
    print(f"\n{'Expense Summary':^36}")
    print("\nLowest Expense(s)")
    print("-" * 36)
    for expense in lowest:
        print(f"{expense['type'][:20]:<20} ${expense['amount']:>13,.2f}")
    print("\nHighest Expense(s)")
    print("-" * 36)
    for expense in highest:
        print(f"{expense['type'][:20]:<20} ${expense['amount']:>13,.2f}")
    print("\nTotal Amount")
    print("-" * 36)
    print(f"{'TOTAL: ':>20} ${total:13,.2f}")


def get_expenses() -> List[Dict[str, float]]:
    """
    Collects user expenses and returns a list of dictionaries with expense
    type and amount.

    Returns:
        List[Dict[str, float]]: A list of dictionaries where each dictionary
        has:
            - "type" (str): The expense type.
            - "amount" (float): The expense amount.
    """
    #   Initialize expenses.
    expenses = []

    #   Give user instructions.
    print(f"\nPlease enter each monthly expense type and amount.\n" +
          "To stop, leave the type field empty and press Enter.\n")

    #   Loop until user enters no type.
    while True:
        #   Retrieve expense type.
        expense_type = get_expense_type()

        #   If no expense type was entered, exit loop.
        if not expense_type:
            break

        #   Retrieve expense amount.
        expense_amount = get_expense_amount()

        #   Store the valid expense as a dictionary in expenses.
        expenses.append({
            "type": expense_type,
            "amount": expense_amount
        })

    #   Return expenses.
    return expenses


def get_expense_type() -> str:
    """
    Prompts the user to enter an expense type and returns the cleaned input.

    Returns:
        str: The trimmed expense type entered by user.
    """
    #   Get expense type from user input.
    prompt_text = f"{'Expense Type:':<20}  "
    expense_type_input = input(prompt_text)

    #   Trim whitespace from expense type.
    expense_type_clean = expense_type_input.strip()

    #   Return cleaned expense type.
    return expense_type_clean


def get_expense_amount() -> float:
    """
    Prompts the user to enter a valid expense amount and returns it as a
    float.

    Returns:
        float: The validated positive expense amount entered by the user.
    """
    #   Create prompt text.
    prompt_text = f"{'Expense Amount:':<20} $"

    #   Loop until user enters valid amount.
    while True:
        #   Retrieve expense amount from user input.
        expense_amount_input = input(prompt_text)

        #   Trim whitespace from expense amount.
        expense_amount_clean = expense_amount_input.strip()

        #   If no expense amount was entered, restart loop.
        if not expense_amount_clean:
            print("Invalid amount. Expense amount is required.")
            continue

        #   Validate expense amount as a positive number. Restart loop if
        #   validation fails.
        try:
            expense_amount = float(expense_amount_clean)
            if expense_amount <= 0:
                print("Invalid amount. Expense amount must be positive.")
                continue
        except ValueError:
            print("Invalid amount. Expense amount must be numeric.")
            continue

        #   Expense amount is valid. Return it.
        return expense_amount


def get_lowest(expenses: List[Dict[str, float]]) -> List[Dict[str, float]]:
    """
        Finds the expense(s) with the lowest amount.

        Args:
            expenses (List[Dict[str, float]]): A list of dictionaries where
            each dictionary contains:
                - "type" (str): The expense type.
                - "amount" (float): The expense amount.

        Returns:
            List[Dict[str, float]]: A list containing all expense(s) with the
            lowest amount. Returns an empty list if expenses is empty.
        """
    #   If expenses is empty, return an empty list.
    if not expenses:
        return []

    #   Find the minimum expense amount.
    lowest_amount = reduce(lambda low, expense:
                           min(low, expense["amount"]),
                           expenses,
                           expenses[0]["amount"])

    #   Get all expenses that match the minimum amount.
    lowest_expenses = [expense for expense in expenses
                       if expense["amount"] == lowest_amount]

    #   Return lowest expenses.
    return lowest_expenses


def get_highest(expenses: List[Dict[str, float]]) -> List[Dict[str, float]]:
    """
    Finds the expense(s) with the highest amount.

    Args:
        expenses (List[Dict[str, float]]): A list of dictionaries where each
            dictionary contains:
            - "type" (str): The expense type.
            - "amount" (float): The expense amount.

    Returns:
        List[Dict[str, float]]: A list containing all expense(s) with the
        highest amount. Returns an empty list if expenses is empty.
    """
    #   If expenses is empty, return an empty list.
    if not expenses:
        return []

    #   Determine the maximum expense amount.
    highest_amount = reduce(lambda high, expense:
                            max(high, expense["amount"]),
                            expenses,
                            expenses[0]["amount"])

    #   Get all expenses that match the maximum amount.
    highest_expenses = [expense for expense in expenses
                        if expense["amount"] == highest_amount]

    #   Return highest expenses.
    return highest_expenses


def get_total(expenses: List[Dict[str, float]]) -> float:
    """
    Calculates the sum total of all expense amounts.

    Args:
        expenses (List[Dict[str, float]]): A list of dictionaries where each
        dictionary contains:
            - "type" (str): The expense type.
            - "amount" (float): The expense amount.

    Returns:
        float: The sum of all expense amounts. Returns 0.0 if the list is
        empty.
    """
    #   Sum up the expense amounts.
    total = reduce(lambda subtotal, expense:
                   subtotal + expense["amount"],
                   expenses,
                   0.0)

    #   Return sum total.
    return total


if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
