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
    https://github.com/JosephDSullivan/COP2373/blob/main/src/chapter12/jsulli40_chapter12_assignment01.py

Problem Description
    In this assignment, you will utilize numpy to analyze student grades
    stored in a CSV file. You will perform various statistical calculations
    and operations to gain insights into the dataset. This assignment will
    help you practice data manipulation and analysis using numpy arrays.
    Instructions:
    Use your CSV file from your Programming Exercise CSV in Week 7. (The file
    should have at least 10 students in it, so rerun your code to have at
    least 10 if needed).
    Load the data from the CSV file into a numpy array.
    Print the first few rows of the dataset to understand its structure.
    Calculate and print the following statistics for each exam (columns):
        Mean (average)
        Median
        Standard deviation
        Minimum
        Maximum
    Calculate and print the overall statistics for the entire dataset (all
    exams combined):
        Mean (average) grade across all exams
        Median grade across all exams
        Standard deviation of grades across all exams
        Minimum grade across all exams
        Maximum grade across all exams
    Determine and print the number of students who passed and failed each
    exam. Consider a passing grade as 60 or above.
    Calculate and print the overall pass percentage across all exams.
    You should have at least two functions, but you can have more.
    Submit your .py file and the .csv file in this assignment and in your
    repository.
    You DO NOT NEED a technical design document for this assignment.
"""

import csv
from typing import List, Tuple

import numpy as np

DATA_FILE_NAME: str = "grades.csv"
"""
CSV file name used to store student grade records.
"""

PASSING_GRADE: int = 60
"""
Lowest grade which results in a passing grade.
"""


def main():
    """
    Entry function for when code is invoked directly.

    Load data from CSV, calculate statistics for each exam and for all exams
    combined, and display results to user.
    """
    #   Load all data from csv.
    all_data = load_data()

    #   Extract exam data from all data (ignore col 0-1, load col 2-4.
    exam_data_list = []
    for row in all_data:
        exam_data_list.append([int(row[2]), int(row[3]), int(row[4])])

    #   Convert exam data list into np array.
    exam_data_array = np.array(exam_data_list)

    #   Calculate statistics for each exam.
    exam_statistics = calculate_exam_statistics(exam_data_array)

    #   Calculate statistics for all exams.
    overall_statistics = calculate_overall_statistics(exam_data_array)

    #   Calculate pass / fail statistics
    pass_fail_counts, pass_percentage = calculate_pass_fail(exam_data_array)

    #   Display the results
    exams = ['Exam 1', 'Exam 2', 'Exam 3']
    print("Exam Statistics:")
    for i, exam in enumerate(exams):
        print(f"\n{exam}:")
        print(f"\tMean:\t{exam_statistics[0][i]:.2f}")
        print(f"\tMedian:\t{exam_statistics[1][i]:.2f}")
        print(f"\tStdDev:\t{exam_statistics[2][i]:.2f}")
        print(f"\tMin:\t{exam_statistics[3][i]}")
        print(f"\tMax:\t{exam_statistics[4][i]}")

    print("\nOverall Statistics (All Exams Combined):")
    print(f"\tMean:\t{overall_statistics[0]:.2f}")
    print(f"\tMedian:\t{overall_statistics[1]:.2f}")
    print(f"\tStdDev:\t{overall_statistics[2]:.2f}")
    print(f"\tMin:\t{overall_statistics[3]}")
    print(f"\tMax:\t{overall_statistics[4]}")

    print("\nPass/Fail Statistics:")
    for i, exam in enumerate(exams):
        print(f"\n{exam}:")
        print(f"\tStudents Passed:\t{pass_fail_counts[i]}")
        print(f"\tPass Percentage:\t{pass_percentage[i]:.2f}%")


def load_data() -> List[List[str]]:
    """
    Load the grades data from a CSV file into a list of lists.

    Returns:
        List[List[str]]: List of lists containing student data (First Name,
            Last Name, Exam 1, Exam 2, Exam 3).
    """
    data = []
    try:
        with open(DATA_FILE_NAME, mode='r', encoding='utf-8',
                  newline='') as file:
            reader = csv.reader(file)
            #   Skip header row.
            next(reader)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("Error: No existing data file found. Exiting program.")
        exit(1)
    return data


def calculate_exam_statistics(exam_data: np.ndarray) -> Tuple[
    np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Calculate the mean, median, standard deviation, minimum, and maximum
    for each exam.

    Args:
        exam_data (np.ndarray): Np array of exam scores.

    Returns:
        Tuple: Mean, median, standard deviation, minimum, and maximum for each
            exam.
    """
    #   Calculate staticstics for each column of exams.
    mean = np.mean(exam_data, axis=0)
    median = np.median(exam_data, axis=0)
    std_dev = np.std(exam_data, axis=0)
    min_score = np.min(exam_data, axis=0)
    max_score = np.max(exam_data, axis=0)

    #   Return tuple of arrays for statistics.
    return mean, median, std_dev, min_score, max_score


def calculate_overall_statistics(exam_data: np.ndarray) -> Tuple[
    float, float, float, float, float]:
    """
    Calculate the mean, median, standard deviation, minimum, and maximum for
    all exams combined.

    Args:
        exam_data (np.ndarray): Np array of exam scores.

    Returns:
        Tuple: Mean, median, standard deviation, minimum, and maximum for all
            exams combined.
    """
    #   Calculate staticstics for all exams combined.
    all_scores = exam_data.flatten()
    mean = np.mean(all_scores)
    median = np.median(all_scores)
    std_dev = np.std(all_scores)
    min_score = np.min(all_scores)
    max_score = np.max(all_scores)

    #   Return tuple of floats for statistics.
    return mean, median, std_dev, min_score, max_score


def calculate_pass_fail(exam_data: np.ndarray) -> Tuple[
    np.ndarray, np.ndarray]:
    """
    Calculate the number of students passing vs failing each exam.

    Args:
        exam_data (np.ndarray): Np array of exam scores.

    Returns:
        Tuple: Number of students passing each exam, pass percentage for each exam.
    """
    pass_fail_counts = np.sum(exam_data >= PASSING_GRADE, axis=0)
    total_students = exam_data.shape[0]
    pass_percentage = (pass_fail_counts / total_students) * 100

    return pass_fail_counts, pass_percentage


if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
