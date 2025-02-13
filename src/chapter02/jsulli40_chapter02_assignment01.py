#!/usr/bin/env python3
"""
This program is designed to detect spam in an email message text.

Author
    Joseph D Sullivan <JSulli40@Student.SCF.edu>

Date
    February 7, 2025

Chapter
    02

Assignment
    01

Repository
    https://github.com/JosephDSullivan/COP2373/blob/main/src/chapter02/jsulli40_chapter02_assignment01.py

Problem Description
    Spam (or junk email) costs U.S. organizations billions of dollars a year
    in spam-prevention software, equipment, network resources, bandwidth, and
    lost productivity. Research online some of the most common spam email
    messages and words. Create a list of 30 words and phrases commonly found
    in spam messages. Write an application in which the user enters an email
    message. Then your application will scan the message for each of the 30
    keywords or phrases. For each occurrence of one of these within the
    message, add a point to the message's "spam score". Next, rate the
    likelihood that the message is spam, based on the number of points
    received. Display the user's spam score, the likelihood message that it is
    spam, and the words/phrases which caused it to be spam.
    You should have at least two functions, but you can have more.
    You must also have a technical design document (refer to the Submitting
    Assignments Module).
    Submit both your .py file and .doc/.docx file in this assignment and these
    files must also be in your repository."""

from typing import List, Tuple

SPAM_MAX_SCORE_UNLIKELY: float = 1.0
"""Maximum spam score allowed for category Unlikely."""

SPAM_MAX_SCORE_LOW: float = 3.0
"""Maximum spam score allowed for category Low."""

SPAM_MAX_SCORE_MEDIUM: float = 5.0
"""Maximum spam score allowed for category Medium."""

SPAM_MAX_SCORE_HIGH: float = 7.0
"""Maximum spam score allowed for category High."""


def main() -> None:
    """
    Entry function for when code is invoked directly.

    Returns:
        None
    """
    #   Get email message from user.
    email_message = get_email_message()

    #   Retrieve spam phrases.
    spam_phrases = get_spam_phrases()

    #   Create output text to display results.
    output = f"\nSpam Likelihood Calculation\n"

    #   Retrieve spam counts for email message.
    spam_counts = get_spam_counts(email_message, spam_phrases)

    #   If there is at least one item in spam counts, then add that
    #   information to output text.
    if len(spam_counts):
        output += f"\n{'PHRASES':<40}{'OCCURRENCES':<20}\n"
        output += f"{'-------':<40}{'-----------':<20}\n"
        for spam_phrase, count in spam_counts:
            output += f"{spam_phrase:<40}{count:>11}\n"
        output += f"\n"

    #   Calculate spam score from spam counts.
    spam_score = get_spam_score(spam_counts)

    #   Calculate spam likelihood from spam score.
    spam_likelihood_text = get_spam_likelihood_text(spam_score)

    #   Add final score and likelihood to output text.
    output += f"\n"
    output += f"{'SCORE:':<15}{spam_score:<20.0f}\n"
    output += f"{'LIKELIHOOD:':<15}{spam_likelihood_text:<20}"

    #   Display output text.
    print(output)


def get_email_message() -> str:
    """
    Retrieves email message text.

    Returns:
        str: Email message text.
    """
    #   Create prompt message text.
    prompt = f"\nPlease enter your email message: "

    #   Retrieve email message text from user and return it.
    email_message = input(prompt)
    return email_message


def get_spam_phrases() -> List[str]:
    """
    Retrieves words / phrases commonly found in spam email.

    Returns:
        List[str]: A sorted list of common spam phrases.
    """
    #   The following list was compiled from multiple sources. Please see the
    #   following files for details:
    #       src/chapter02/source_activecampaign.com.pdf
    #       src/chapter02/source_lix-it.com.pdf
    #       src/chapter02/source_zerobounce.net.pdf
    #       src/chapter02/spam_phrases.xlsx
    phrases = [
        "free", "cash", "credit", "money", "order", "offer", "ad", "click",
        "deal", "debt", "income", "win", "100%", "bonus", "rates", "sale",
        "guaranteed", "invest", "sales", "trial", "buy", "dear",
        "investment", "lifetime", "obligation", "prize", "save big",
        "solution", "urgent", "winner", "#1", "$$$", "cash bonus", "chance",
        "cheap", "clearance", "click here", "compare", "increase sales",
        "instant", "limited time", "miracle", "no obligation",
        "no strings attached", "opt in", "quote", "refund", "sample",
        "satisfaction", "100% free", "100% satisfied", "act now",
        "affordable", "all new", "amazing", "apply now", "as seen on",
        "bargain", "be your own boss", "best price", "big bucks",
        "buy direct", "call now", "cancel", "cards accepted", "certified",
        "click below", "compare rates", "congratulations", "dear friend",
        "discount", "don’t delete", "don’t hesitate", "earnings",
        "eliminate bad credit", "exclusive deal", "extra cash",
        "extra income", "fantastic", "free consultation", "free gift",
        "free membership", "free money", "free preview", "free quote",
        "free sample", "free trial", "full refund", "get started now",
        "important information regarding", "join millions", "link", "loan",
        "lowest price", "make money", "marketing solution", "mass email",
        "meet singles", "name brand", "new customers only", "no catch",
        "no cost", "no gimmick", "no hidden cost", "no questions asked",
        "once in a lifetime", "one hundred percent", "open", "order now",
        "order shipped", "password", "promise", "risk free",
        "satisfaction guaranteed", "save big money", "score",
        "sign up free", "social security number", "special promotion",
        "terms and conditions", "unlimited", "weight loss",
        "what are you waiting for?", "while supplies last",
        "will not believe your eyes", "work from home",
        "you have been selected", "your income"
    ]
    #   Normalize each phrase by explicitly converting into a string, trimming
    #   white space, and converting to lowercase.
    cleaned_phrases = [str(phrase).strip().lower() for phrase in phrases]
    #   Return phrases, sorted alphabetically.
    return sorted(cleaned_phrases)


def get_spam_counts(email_message: str,
                    spam_phrases: List[str]
                    ) -> List[Tuple[str, int]]:
    """
    Calculates counts of each spam phrase found in email message.

    Args:
        email_message (str): The email message text.
        spam_phrases (List[str]): A list of spam phrases to search for.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains
            a spam phrase and its count in the email message.
    """
    #   Initialize list containing spam phrases found.
    spam_phrases_found: List[Tuple[str, int]] = []

    #   Convert email message to lowercase so search is case-insensitive.
    email_message_lower = email_message.lower()

    #   Iterate through each spam phrase and count occurrences in email
    #   message.
    for spam_phrase in spam_phrases:
        count = email_message_lower.count(spam_phrase)
        #   If any spam phrase is found in email message, then add that phrase
        #   and the number of times that phrase was found in email message to
        #   spam phrases found list.
        if count > 0:
            spam_phrases_found.append((str(spam_phrase), int(count)))

    #   Return spam phrases found.
    return spam_phrases_found


def get_spam_score(spam_counts: List[Tuple[str, int]]
                   ) -> float:
    """
    Calculates spam score given a list of spam phrase counts.

    Args:
        spam_counts (List[Tuple[str, int]]): A list of tuples where each tuple
            contains a spam phrase and its count in the email message.

    Returns:
        float: Total spam score.
    """
    #   Initialize spam score for the email message.
    spam_score = 0.0

    #   Iterate through spam counts and add each count to spam score.
    for _, count in spam_counts:
        spam_score += float(count)

    #   Return spam score.
    return spam_score


def get_spam_likelihood_text(spam_score: float
                             ) -> str:
    """
    Calculates spam likelihood text based on spam score and categories created
    via module constants SPAM_MAX_SCORE_*.

    Args:
        spam_score (float): Spam score to calculate likelihood text for.

    Returns:
        str: Spam likelihood text.

    Raises:
        ValueError: If spam score is not numeric or is less than zero.
    """
    #   Verify spam score is numeric. If not, raise error.
    if not isinstance(spam_score, (int, float)):
        raise ValueError("Spam score must be a numeric value.")
    #   Verify spam score is nonnegative. If not, raise error.
    if spam_score < 0:
        raise ValueError('Spam score must be greater than zero.')
    #   Spam score is valid. Find the category based on constants and return
    #   category name.
    elif spam_score <= SPAM_MAX_SCORE_UNLIKELY:
        return "Unlikely"
    elif spam_score <= SPAM_MAX_SCORE_LOW:
        return "Low"
    elif spam_score <= SPAM_MAX_SCORE_MEDIUM:
        return "Medium"
    elif spam_score <= SPAM_MAX_SCORE_HIGH:
        return "High"
    else:
        return "Extremely Likely"


if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
