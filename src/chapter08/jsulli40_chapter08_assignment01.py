#!/usr/bin/env python3
"""
tbd

Author
    Joseph D Sullivan <JSulli40@Student.SCF.edu>

Date
    March 14, 2025

Chapter
    08

Assignment
    01

Repository
    https://github.com/JosephDSullivan/COP2373/blob/main/src/chapter08/jsulli40_chapter08_assignment01.py

Problem Description
    An instructor teaches a class in which each student takes three exams. The
    instructor would like to store this information in a file named grades.csv
    for later use. Create a program that allows an instructor to input how
    many students they want to enter. Then enter each student’s first name and
    last name as strings and the student’s three exam grades as integers. Use
    the csv module to write each record into the grades.csv file and have a
    header of First Name, Last Name, Exam 1, Exam 2 and Exam3. Each student
    should be a record in the grades.csv file.
    Once the file is created, create a separate program to read the grades.csv
    file and display the data in tabular format. Implement the with keyword.
    You may need to refer back to Chapter 5 for formatting.
    Each of these 2 programs should be separate functions so you have at least
    two functions for this assignment, but you can have more.
    You must also have a technical design document (refer to the Submitting
    Assignments Module).
    Submit both your .py file and .doc/.docx file in this assignment and these
    files must also be in your repository.
    ***The .csv file for this assignment should also be in your repository.
"""

from typing import Optional


def main():
    """"""
    print(f"\n\n")
    pass


def get_grade():
    """"""
    pass


def get_grades():
    """"""
    pass


def show_grades():
    """"""


def add_grades():
    """"""
    pass


def get_int(prompt: str = "Please enter an integer: ",
            lbound: Optional[int] = None,
            ubound: Optional[int] = None,
            repeat_until_valid: bool = True
            ) -> Optional[int]:
    """
    Prompt the user to enter an integer, validate it, and return it.

    Args:
        prompt (str): The message displayed to the user when asking for input.
            Defaults to "Please enter an integer: ".
        lbound (int, optional): The lower bound for valid input. Defaults to
            None, representing no lower bound.
        ubound (int, optional): The upper bound for valid input. Defaults to
            None, representing no upper bound.
        repeat_until_valid (bool): Whether to keep prompting until valid input
            is received. Defaults to True.

    Returns:
        Optional[int]: The validated integer input from the user, or None if
            repeat_until_valid is False and input is invalid.
    """
    while True:
        err_message = None
        user_input = input(prompt).strip()

        if not user_input:
            err_message = f"Input cannot be empty."
        else:
            try:
                user_input_int = int(user_input)

                #   Validate bounds. If out of bounds, warn user and reloop.
                if lbound is not None and user_input_int < lbound:
                    err_message = f"Input must be at least {lbound}."
                elif ubound is not None and user_input_int > ubound:
                    err_message = f"Input must be at most {ubound}."
                else:
                    #   Input is valid.
                    return user_input_int

            except ValueError:
                err_message = f"Input must be an integer."

        #   Input is invalid.
        if repeat_until_valid:
            if err_message:
                print(err_message)
        else:
            return None


def get_str(prompt: str = "Please enter a string: ",
            allow_empty_string: bool = False,
            repeat_until_valid: bool = True
            ) -> Optional[str]:
    """
    Prompt the user to enter a string, validate it, and return it.

    Args:
        prompt (str): The message displayed to the user when asking for input.
            Defaults to "Please enter a string: ".
        allow_empty_string (bool): Whether empty strings are allowed. Defaults
            to False.
        repeat_until_valid (bool, optional): Whether to keep prompting until
            valid input is received. Defaults to True.

    Returns:
        Optional[str]: The validated string input from the user, or None if
            repeat_until_valid is False and input is invalid.

    TODO:
        Implement RegEx matching for validation. There has to be a cool way to
        implement accepting any number of regex patterns and only accept
        strings which match all regex patterns. I don't know how. Yet.
    """
    while True:
        user_input = input(prompt).strip()

        if not user_input and not allow_empty_string:
            #   Input is invalid.
            if repeat_until_valid:
                print(f"Input cannot be empty.")
                continue
            return None

        #   Input is valid.
        return user_input


if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
