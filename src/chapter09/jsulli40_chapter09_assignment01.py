#!/usr/bin/env python3
"""
This module models a basic bank account, with methods for setting the interest
rate, withdrawing funds, depositing funds, reporting balance, and calculating
interest.

Author
    Joseph D Sullivan <JSulli40@Student.SCF.edu>

Date
    March 30, 2025

Chapter
    09

Assignment
    01

Repository
    https://github.com/JosephDSullivan/COP2373/blob/main/src/chapter09/jsulli40_chapter09_assignment01.py

Problem Description
    Create a BankAcct Class that contains at least the following state
    information: name, account number, amount and interest rate. In addition
    to an __init__ method, the class should support methods for adjusting the
    interest rate, for withdrawing and depositing, and for giving a balance.
    You should also include a method to calculate the interest based on the
    number of days. Use the __str__ method to display balances and interest
    amounts. Create a test function to test the different methods in the
    BankAcct Class.
    The class and test function should be in one .py file.
    Submit your .py file in this assignment and in your repository.
    You DO NOT NEED a technical design document for this assignment.
"""

from decimal import Decimal


def main():
    """
    Entry function for when code is invoked directly.
    """
    test_bank_acct()


class BankAcct:
    """
    A class that represents a bank account.
    """

    def __init__(self,
                 name: str,
                 account_number: str,
                 initial_deposit: Decimal,
                 interest_rate: Decimal
                 ) -> None:
        """
        Initialize a bank account.

        Args:
            name (str): The name of the account holder. Required.
            account_number (str): The account number. Required.
            initial_deposit (Decimal): The initial deposit amount. Must be
                nonnegative.
            interest_rate (Decimal): The interest rate. Must be nonnegative.
        """
        #   Validate account information.
        if not name:
            raise ValueError(f"Name is required and cannot be empty.")
        if not account_number:
            raise ValueError(f"Account number is required and cannot be " +
                             f"empty.")
        if initial_deposit < 0:
            raise ValueError(f"Initial deposit ({str(interest_rate)}) " +
                             f"cannot be negative.")
        if interest_rate < 0:
            raise ValueError(f"Interest rate ({str(interest_rate)}) " +
                             f"cannot be negative.")
        self.name = name
        self.account_number = account_number
        self.balance = Decimal(initial_deposit)
        self.interest_rate = Decimal(interest_rate)

    def __str__(self
                ) -> str:
        """
        Return account information in tabular format.

        Returns:
            str: The account information in tabular format.

        """
        #   Return account information in tabular format.
        return (f"Account Holder: \t{self.name}\n"
                f"Account Number: \t{self.account_number}\n"
                f"Current Balance:\t${self.balance:.2f}\n"
                f"Interest Rate:  \t{self.interest_rate:.2f}%")

    def set_interest_rate(self,
                          interest_rate: Decimal
                          ) -> None:
        """
        Setter method for interest rate.

        Args:
            interest_rate (Decimal): The interest rate. Must be nonnegative.
        """
        #   Validate interest rate.
        try:
            interest_rate = Decimal(interest_rate)
        except ValueError:
            raise ValueError(f"Interest rate ({str(interest_rate)}) must " +
                             f"be numeric.")
        if interest_rate < 0:
            raise ValueError(f"Interest rate ({str(interest_rate)}) cannot " +
                             f"be negative.")

        #   Adjust interest rate.
        self.interest_rate = interest_rate

    def make_deposit(self,
                     amount: Decimal
                     ) -> None:
        """
        Deposit funds into the account.

        Args:
            amount (Decimal): The deposit amount. Must be nonnegative.
        """
        #   Validate amount.
        try:
            amount = Decimal(amount)
        except ValueError:
            raise ValueError(f"Amount ({str(amount)}) must be numeric.")
        if amount < 0:
            raise ValueError(f"Amount ({str(amount)}) cannot be negative.")

        #   Adjust balance.
        self.balance += amount

    def make_withdraw(self,
                      amount: Decimal
                      ) -> None:
        """
        Withdraw funds int the account.

        Args:
            amount (Decimal): The withdrawal amount. Must be nonnegative.
        """
        #   Validate amount.
        try:
            amount = Decimal(amount)
        except ValueError:
            raise ValueError(f"Amount ({str(amount)}) must be numeric.")
        if amount < 0:
            raise ValueError(f"Amount ({str(amount)}) cannot be negative.")
        if amount > self.balance:
            raise ValueError(f"Amount ({str(amount)}) cannot be greater " +
                             f" than the balance ({self.balance}).")

        #   Adjust balance.
        self.balance -= amount

    def get_balance(self
                    ) -> Decimal:
        """
        Getter method for balance.

        Returns:
            Decimal: The balance.

        """
        return self.balance

    def calculate_interest_amount(self,
                                  days: int,
                                  ) -> Decimal:
        """
        Calculate interest amount accumulated over a given number of days.

        Args:
            days (int): The number of days to calculate interest amount for.
                Must be nonnegative.

        Returns:
            Decimal: The interest amount accumulated.
        """
        #   Validate days.
        try:
            days = Decimal(days)
        except ValueError:
            raise ValueError(f"Days ({str(days)}) must be numeric.")
        if days < 0:
            raise ValueError(f"Days ({str(days)}) cannot be negative.")

        #   Calculate interest amount and return it.
        daily_rate = (self.interest_rate / 100) / 365
        interest = self.balance * daily_rate * days
        return interest


def test_bank_acct():
    #   Create an account.
    acct = BankAcct(name="Joseph Sullivan",
                    account_number="123456789",
                    initial_deposit=1000000,
                    interest_rate=3.6)
    print(f"\nNEW ACCOUNT")
    print(acct)

    #   Calculate interest amount for 100 days.
    print(f"\nInterest accumulated over 100 days:\t" +
          f"{acct.calculate_interest_amount(days=100)}")

    #   Change interest rate.
    acct.set_interest_rate(4.8)
    print(f"\nCHANGE INTEREST RATE")
    print(acct)

    #   Calculate interest amount for 100 days.
    print(f"\nInterest accumulated over 100 days:\t" +
          f"{acct.calculate_interest_amount(days=100)}")

    #   Deposit $200,000.
    acct.make_deposit(amount=200000)
    print(f"\nAFTER DEPOSIT")
    print(acct)

    #   Withdraw $120,000.
    acct.make_withdraw(amount=120000)
    print(f"\nAFTER WITHDRAWAL")
    print(acct)

    #   Current balance.
    print(f"\nCurrent balance:\t{acct.get_balance()}")


if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
