#!/usr/bin/env python3
"""
Collect user input for telephone number, social security number, and zip code;
and validate using regular expressions.

Author
    Joseph D Sullivan <JSulli40@Student.SCF.edu>

Date
    March 01, 2025

Chapter
    06

Assignment
    06

Repository
    https://github.com/JosephDSullivan/COP2373/blob/main/src/chapter06/jsulli40_chapter06_assignment06.py

Problem Description
    Create functions to validate phone numbers, social security numbers and
    zip codes using regular expressions. Create a main function to get input
    from a user and then displaying if the phone number, social security
    number and zip code they entered is valid.
    Be sure to test the functions with various inputs, including valid and
    invalid examples, to ensure the correctness of the regular expressions.
    You must also have a technical design document (refer to the Submitting
    Assignments Module).
    Submit both your .py file and .doc/.docx file in this assignment and these
    files must also be in your repository.
"""

import re

REGEX_TELE_NUM = re.compile(r"^\(?(?P<area_code>\d{3})?\)?[ -.]?" +
                            r"(?P<telephone_prefix>\d{3})[ -.]?" +
                            r"(?P<line_number>\d{4})$")
"""
Regular expression Pattern to validate telephone number.

Allows:
    (###) ###-####
    ###-###-####
    ###.###.####
    ##########
    ###-####
    ###.####
    #######
"""

REGEX_SSN = re.compile(r"^(?P<area_num>\d{3})[ -]?" +
                       r"(?P<group_num>\d{2})[ -]?" +
                       r"(?P<serial_num>\d{4})$")
"""
Regular expression Pattern to validate social security number.

Allows:
    ###-##-####
    ### ## ####
    #########
"""

REGEX_ZIP = re.compile(r"^(?P<zip_code>\d{5})[ -]?" +
                       r"(?P<plus4>\d{4})?$")
"""
Regular expression Pattern to validate zip code.

Allows:
    #####-####
    ##### ####
    #####
"""


def main():
    """
    Entry function for when code is invoked directly.

    Retrieve telephone number, social security number, and zip code from
    user, validate each input, and display the results to user.

    Returns:
        None
    """
    #   Retrieve telephone number from user input.
    prompt = "Telephone Number:"
    tele_num = input(f"{prompt:<25}").strip()

    #   Retrieve social security number from user input.
    prompt = "Social Security Number:"
    ssn = input(f"{prompt:<25}").strip()

    #   Retrieve zip code from user input.
    prompt = "Zip Code:"
    zip_code = input(f"{prompt:<25}").strip()

    #   Validate input.
    is_valid_tele_num = validate_tele_num(tele_num)
    is_valid_ssn = validate_ssn(ssn)
    is_valid_zip = validate_zip(zip_code)

    #   Display results.
    output = f"\n\n"
    output += f"{'Type':<25}{'Data':<15}{'Valid':<5}\n"
    output += f"-" * (25 + 15 + 5) + f"\n"
    output += f"{'Telephone number':<25}{tele_num:<15.15}{'Yes' if
        is_valid_tele_num else 'No':<5}\n"
    output += f"{'Social security number':<25}{ssn:<15.15}{'Yes' if
        is_valid_ssn else 'No':<5}\n"
    output += f"{'Zip code':<25}{zip_code:<15.15}{'Yes' if
        is_valid_zip else 'No':<5}\n"
    print(output)


def validate_tele_num(tele_num: str) -> bool:
    """
    Validate a telephone number.

    Utilizes regular expression Pattern REGEX_TELE_NUM to validate telephone
    number. If the pattern is found anywhere in the telephone number, then it
    is considered valid.

    Args:
        tele_num (str): The telephone number to validate.

    Returns:
        bool: True if the telephone number is valid, False otherwise.
    """
    match = re.search(REGEX_TELE_NUM, tele_num)
    return bool(match)


def validate_ssn(ssn: str) -> bool:
    """
    Validate a social security number.

    Utilizes regular expression Pattern REGEX_SSN to validate social security
    number. If the pattern is found anywhere in the social security number,
    then it is considered valid.

    Args:
        ssn (str): The social security number to validate.

    Returns:
        bool: True if the social security number is valid, False otherwise.
    """
    match = re.search(REGEX_SSN, ssn)
    return bool(match)


def validate_zip(zip_code: str) -> bool:
    """
    Validate a zip code.

    Utilizes regular expression Pattern REGEX_ZIP to validate zip code. If the
    pattern is found anywhere in the zip code, then it is considered valid.

    Args:
        zip_code (str): The zip code to validate.

    Returns:
        bool: True if the zip code is valid, False otherwise.
    """
    match = re.search(REGEX_ZIP, zip_code)
    return bool(match)


if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
