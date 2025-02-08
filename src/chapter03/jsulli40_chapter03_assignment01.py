#!/usr/bin/env python3
""" This program is to detect spam in an email text.

Author
    Joseph D Sullivan <JSulli40@Student.SCF.edu>

Date
    February 7, 2025

Chapter
    03

Assignment
    01

Repository
    https://github.com/JosephDSullivan/COP2373/blob/main/src/chapter03/jsulli40_chapter03_assignment01.py

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
    files must also be in your repository.
"""

#   Import(s)
from typing import List, Tuple

#   Constant(s)
#   Maximum spam scores defining each spam likelihood category. Note that
#   these values are inclusive.
SPAM_MAX_SCORE_UNLIKELY: float = 1.0
SPAM_MAX_SCORE_LOW: float = 3.0
SPAM_MAX_SCORE_MEDIUM: float = 5.0
SPAM_MAX_SCORE_HIGH: float = 7.0

#   Variable(s)


def main() -> None:
    """
    Entry function for when code is invoked directly.

    Args:


    Returns:
        None
    """
    #   tbd
    email_message = """Dear Friend,

Congratulations! You have been selected to receive an amazing deal that you won’t want to miss. For a limited time, you can get a 100% free trial of our exclusive service – no obligation, no strings attached!

✔ Guaranteed results or your money back!
✔ Increase sales with our proven marketing solution!
✔ Save big on your next order – don’t hesitate!

But that’s not all! Sign up today and receive a cash bonus of $50 – an instant reward just for joining. This is a once in a lifetime opportunity to invest in your future and make money with ease.

💰 No gimmick, no hidden costs – just free money to get you started!
📦 Hurry! While supplies last, claim your free gift today!
🔗 Click here to opt in and get started now!

Don’t delete this email – this is your chance to grab an exclusive deal before it’s gone!

Best regards,
[Your Company Name]
📞 Call now for more details!

P.S. We offer risk-free options with a full refund if you’re not 100% satisfied. What are you waiting for? 🎁

Extra Bonus!"""
    spam_phrases = get_spam_phrases()
    spam_counts = get_spam_counts(email_message, spam_phrases)
    spam_score = get_spam_score(spam_counts)
    print(spam_phrases)
    print(spam_counts)
    print(spam_score)
    pass

def get_spam_phrases() -> List[str]:
    """
    Returns a list of phrases commonly found in spam email.

    Returns:
        List[str]: A sorted list of common spam phrases.
    """
    #   The following list was compiled from multiple sources. Please see the
    #   following files for details:
    #       src/chapter03/source_activecampaign.com.pdf
    #       src/chapter03/source_lix-it.com.pdf
    #       src/chapter03/source_zerobounce.net.pdf
    #       src/chapter03/spam_phrases.xlsx
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
    #   Normalize spam phrases by explicitly converting into a string,
    #   trimming white space, and converting to lowercase.
    cleaned_phrases = [str(phrase).strip().lower() for phrase in phrases]
    #   Return list, sorted alphabetically.
    return sorted(cleaned_phrases)


def get_spam_counts(email_message: str,
                    spam_phrases: List[str]
                   ) -> List[Tuple[str, int]]:
    """
    Calculates counts of each spam phrase found in email message.

    Args:
        email_message (str): The email message text.
        spam_phrases (list): A list of spam phrases to search for.

    Returns:
        List[Tuple[str, int]]: A list of tuples where each tuple contains
            a spam phrase and its count in the email message.
    """
    #   List containing found phrases and their count.
    spam_phrases_found: List[Tuple[str, int]] = []

    #   Convert email message to lowercase so search is case-insensitive.
    email_message_lower = email_message.lower()
    #   Iterate through each spam phrase and count occurrences in email
    #   message.
    for spam_phrase in spam_phrases:
        count = email_message_lower.count(spam_phrase)

        if count > 0:
            #   Spam phrase found in email message. Add the phrase and the
            #   count of that phrase to phrases found list.
            spam_phrases_found.append((str(spam_phrase), int(count)))

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
    #   Spam score for the email message.
    spam_score = 0.0

    #   Iterate through spam counts and add each count to spam score.
    for _, count in spam_counts:
        spam_score += count

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
    """


if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass