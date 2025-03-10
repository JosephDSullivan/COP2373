#!/usr/bin/env python3
"""
Collect user input for paragraph text, split input into sentences using
regular expressions, and display sentences to user.

Author
    Joseph D Sullivan <JSulli40@Student.SCF.edu>

Date
    March 09, 2025

Chapter
    07

Assignment
    07

Repository
    https://github.com/JosephDSullivan/COP2373/blob/main/src/chapter07/jsulli40_chapter07_assignment07.py

Problem Description
    Using the code in Section 7.4, write a program that will allow me to enter
    a paragraph, including sentences which begin with numbers. Display each
    individual sentence and the count of sentences in the paragraph.
    You should have at least two functions, but you could have more.
    You must also have a technical design document (refer to the Submitting
    Assignments Module).
    Submit both your .py file and .doc/.docx file in this assignment and these
    files must also be in your repository.
"""

import re
from typing import List

REGEX_SENTENCE = re.compile(pattern="[0-9A-Z].*?[.!?](?= [0-9A-Z]|$)",
                            flags=re.DOTALL | re.MULTILINE)
"""
Regular expression Pattern to match sentences. Modified from book_code_7.4.py.

Allows:
    Matches sentences that start with a number (0-9) or an uppercase letter
        (A-Z).
    Captures everything until a period (.), exclamation (!), or question mark
        (?).
    Ensures that the next character is either an uppercase letter, a number,
        or the end of the string.
    Uses DOTALL and MULTILINE flags to handle multiline input properly.
"""


def main():
    """
    Entry function for when code is invoked directly.

    Retrieve paragraph from user input, split input into sentences. and
    display results.

    Returns:
        None
    """
    #   Retrieve paragraph from user input.
    prompt = "Paragraph:"
    paragraph = input(f"{prompt:<15}").strip()

    #   Split input into sentences.
    sentences = get_sentences(paragraph)

    #   Display results.
    display_sentences(sentences)


def get_sentences(paragraph: str) -> List[str]:
    """
    Extracts sentences from paragraph using REGEX_SENTENCE.

    Args:
        paragraph (str): The paragraph text to get sentences from.

    Returns:
        List[str]: A list of sentences found in paragraph.
    """
    sentences = re.findall(REGEX_SENTENCE, paragraph)
    return sentences


def display_sentences(sentences: List[str]) -> None:
    """
    Display each sentences in sentences, as well as sentence count.

    Args:
        sentences (List[str]): A list of sentences.

    Returns:
        None
    """
    print("\nYour Sentence(s):")
    for sentence in sentences:
        escaped_sentence = repr(sentence.strip())
        print(f"\t{escaped_sentence}")
    print(f"\nSentence Count:\t{len(sentences)}")


if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
