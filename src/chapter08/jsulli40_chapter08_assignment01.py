#!/usr/bin/env python3
"""
This program allows an instructor to store and retrieve student score data.

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

import csv
import re
from dataclasses import dataclass, field
from typing import List, Pattern, Union

DEFAULT_SCORE: float = 0.0
"""
Default exam score if no score is provided.
"""

MIN_SCORE: float = 0.0
"""
Minimum valid exam score.
"""

MAX_SCORE: float = 120.0
"""
Maximum valid exam score.
"""

DATA_FILE_NAME: str = "grades.csv"
"""
CSV file name used to store student grade records.
"""


@dataclass()
class StudentScore:
    """
    Data class representing a single student's exam scores.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        exam01 (float): Score for exam 1.
        exam02 (float): Score for exam 2.
        exam03 (float): Score for exam 3.
    """
    first_name: str
    last_name: str
    exam01: float | None = DEFAULT_SCORE
    exam02: float | None = DEFAULT_SCORE
    exam03: float | None = DEFAULT_SCORE

    def __post_init__(self):
        """
        Validate the student score data.
        """
        #   Verify first name and last name are not empty.
        if not self.first_name:
            raise ValueError("First name is required and cannot be empty.")
        if not self.last_name:
            raise ValueError("Last name is required and cannot be empty.")

        #   Verify all scores are between MIN_SCORE and MAX_SCORE,
        #   inclusive.
        for exam in ["exam01", "exam02", "exam03"]:
            score = getattr(self, exam)
            if score is None:
                setattr(self, exam, DEFAULT_SCORE)
            elif not (MIN_SCORE <= score <= MAX_SCORE):
                raise ValueError(f"{exam} for {self.first_name} " +
                                 f"{self.last_name} must be between " +
                                 f"{MIN_SCORE} and {MAX_SCORE}.")


@dataclass()
class StudentScores:
    """
    List of StudentScore, representing all students' scores.

    Attributes:
        students (List[StudentScore]): A list of StudentScore.
    """
    students: List[StudentScore] = field(default_factory=list)

    def add_student(self, student: StudentScore):
        """
        Adds a StudentScore to the students list and the CSV data file.

        Args:
            student (StudentScore): The StudentScore to add.

        Raises:
            TypeError: If the argument student is not a StudentScore instance.
        """
        #   Validate data.
        if not isinstance(student, StudentScore):
            raise TypeError(f"Only StudentScore instances can be added " +
                            f"to StudentScores.")

        #   Add student to students list.
        self.students.append(student)

        #   Add student to csv data file.
        with open(file=DATA_FILE_NAME, mode='a', encoding='utf-8',
                  newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                head = ["First Name", "Last Name",
                        "Exam 1", "Exam 2", "Exam 3"]
                writer.writerow(head)
            writer.writerow([student.first_name, student.last_name,
                             student.exam01, student.exam02, student.exam03])

    def display_students(self):
        """
        Displays all students' scores in a tabular format.
        """
        #   Display all students in tabular format.
        print(f"\n{'First Name':<30} {'Last Name':<40} " +
              f"{'Exam 1':>8} {'Exam 2':>8} {'Exam 3':>8}")
        print("-" * 98)
        for student in self.students:
            print(
                f"{student.first_name:<30.30} {student.last_name:<40.40} " +
                f"{student.exam01:>8.2f} {student.exam02:>8.2f} " +
                f"{student.exam03:>8.2f}")

    def load_students(self):
        """
        Loads student records from the CSV file into the student list. Warns
        user if file does not exist.
        """
        #   Clear current list before importing.
        self.students.clear()

        #   Open csv data file and import all rows into self.students. If file
        #   not found, warn user.
        try:
            with open(DATA_FILE_NAME, mode='r', encoding='utf-8',
                      newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student_score = StudentScore(
                        first_name=row['First Name'],
                        last_name=row['Last Name'],
                        exam01=float(row['Exam 1']),
                        exam02=float(row['Exam 2']),
                        exam03=float(row['Exam 3'])
                    )
                    self.students.append(student_score)
        except FileNotFoundError:
            print("Warning: No existing data file found.")


def main():
    """
    Entry function for when code is invoked directly.

    Load student scores list, display table, retrieve new student scores,
    redisplay table, repeat until the user exits, and redisplay table one
    final time.
    """
    #   Load student scores list.
    students = StudentScores()
    students.load_students()

    #   Display initial data to user.
    print(f"\nSTUDENT SCORES (INITIAL)")
    students.display_students()

    #   Retrieve number of students to add from user.
    num_student = -1
    while num_student != 0:
        num_student = get_int(prompt=f"\nHow many students would you like " +
                                     f"to add? (Enter 0 to Exit Program)\t",
                              lbound=0)

        #   Display results one final time and exit program if 0 entered.
        if num_student == 0:
            print(f"\nSTUDENT SCORES (FINAL)")
            students.display_students()
            return

        #   Loop for each new student: create new student and append it to
        #   students.
        for _ in range(num_student):
            new_student = get_student()
            students.add_student(new_student)

        #   Display new students list to user.
        print(f"\nSTUDENT SCORES (AFTER +{num_student} STUDENTS)")
        students.display_students()


def get_student() -> StudentScore:
    """
    Retrieves student data from user and create a StudentScore with that data.

    Returns:
        StudentScore: A dataclass instance containing the student's data.
    """
    #   Regular expression Pattern to verify string is not blank.
    regex_nonblank = re.compile(r"^.+$")

    #   Prompt user to enter student score data.
    print(f"Please enter the following details for new student scores:")
    first_name = get_str(prompt=f"\tFirst Name:\t",
                         pattern=regex_nonblank)
    last_name = get_str(prompt=f"\tLast Name:\t",
                        pattern=regex_nonblank)
    exam01 = get_float(prompt=f"\tExam 01:\t",
                       lbound=MIN_SCORE,
                       ubound=MAX_SCORE)
    exam02 = get_float(prompt=f"\tExam 02:\t",
                       lbound=MIN_SCORE,
                       ubound=MAX_SCORE)
    exam03 = get_float(prompt=f"\tExam 03:\t",
                       lbound=MIN_SCORE,
                       ubound=MAX_SCORE)

    #   Return student score data as StudentScore.
    return StudentScore(first_name=first_name, last_name=last_name,
                        exam01=exam01, exam02=exam02, exam03=exam03)


def get_int(prompt: str | None = None,
            lbound: int | None = None,
            ubound: int | None = None,
            repeat_until_valid: bool | None = True
            ) -> int | None:
    """
    Prompt the user to enter an integer, validate input, and return it.

    Args:
        prompt (str | None, optional): The message displayed to the user when
            asking for input. Defaults to None, which represents no prompt.
        lbound (int | None, optional): The lower bound (inclusive) for valid
            input. Defaults to None, which represents no lower bound.
        ubound (int | None, optional): The upper bound (inclusive) for valid
            input. Defaults to None, which represents no upper bound.
        repeat_until_valid (bool | None, optional): Whether to keep prompting
            until valid input is received. Defaults to True.

    Returns:
        int | None: The validated integer input from the user, or None if
            repeat_until_valid is False and input is invalid.
    """

    if repeat_until_valid is None:
        repeat_until_valid = True

    #   Loop until exit.
    while True:
        #   Retrieve input from user.
        user_input = input(prompt or "").strip()
        #   Validate input.
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
                    #   Return validated input.
                    return user_input_int

            except ValueError:
                err_message = f"Input must be an integer."

        #   Input is invalid.
        if repeat_until_valid:
            if err_message:
                print(err_message)
        else:
            return None


def get_float(prompt: str | None = None,
              lbound: float | None = None,
              ubound: float | None = None,
              repeat_until_valid: bool | None = True
              ) -> float | None:
    """
    Prompt the user to enter a float, validate input, and return it.

    Args:
        prompt (str | None, optional): The message displayed to the user when
            asking for input. Defaults to None, which represents no prompt.
        lbound (float | None, optional): The lower bound (inclusive) for valid
            input. Defaults to None, which represents no lower bound.
        ubound (float | None, optional): The upper bound (inclusive) for valid
            input. Defaults to None, which represents no upper bound.
        repeat_until_valid (bool | None, optional): Whether to keep prompting
            until valid input is received. Defaults to True.

    Returns:
        float | None: The validated float input from the user, or None if
            repeat_until_valid is False and input is invalid.
    """
    if repeat_until_valid is None:
        repeat_until_valid = True

    #   Loop until exit.
    while True:
        #   Retrieve input from user.
        user_input = input(prompt or "").strip()

        #   Validate input.
        if not user_input:
            err_message = f"Input cannot be empty."
        else:
            try:
                user_input_f = float(user_input)

                #   Validate bounds. If out of bounds, warn user and reloop.
                if lbound is not None and user_input_f < lbound:
                    err_message = f"Input must be at least {lbound}."
                elif ubound is not None and user_input_f > ubound:
                    err_message = f"Input must be at most {ubound}."
                else:
                    #   Return validated input.
                    return user_input_f

            except ValueError:
                err_message = f"Input must be a float."

        #   Input is invalid.
        if repeat_until_valid:
            if err_message:
                print(err_message)
        else:
            return None


def get_str(prompt: str | None = None,
            pattern: Union[str, Pattern] | None = None,
            repeat_until_valid: bool | None = True
            ) -> str | None:
    """
    Prompt the user to enter a string, validate input, and return it.

    Args:
        prompt (str | None, optional): The message displayed to the user when
            asking for input. Defaults to None, which represents no prompt.
        pattern (Union[str, Pattern] | None, optional): The regular
            expression - as a string or a compiled re.Pattern - to validate
            input. Defaults to None, which represents no validation.
        repeat_until_valid (bool | None, optional): Whether to keep prompting
            until valid input is received. Defaults to True.

    Returns:
        str | None, optional: The validated string input from the user, or
            None if repeat_until_valid is False and input is invalid.
    """
    if repeat_until_valid is None:
        repeat_until_valid = True
    if isinstance(pattern, str):
        pattern = re.compile(pattern)

    #   Loop until exit.
    while True:
        #   Retrieve input from user.
        user_input = input(prompt or "")

        #   Validate input.
        if pattern:
            if not pattern.fullmatch(user_input):
                #   Input is invalid.
                if repeat_until_valid:
                    print(f"Invalid input.")
                    continue
                else:
                    return None

        #   Return validated input.
        return user_input


if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
