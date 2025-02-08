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
from typing import List

#   Constant(s)

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

    print(get_spam_phrases())
    print(get_spam_counts(email_message, spam_phrases))
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
    #   Convert each phrase explicitly into a string, trim white space, and
    #   convert to lowercase.
    cleaned_phrases = [str(phrase).strip().lower() for phrase in phrases]
    #   Return list sorted alphabetically.
    return sorted(cleaned_phrases)


def get_spam_counts(email_message: str,
                    spam_phrases: list
                   ) -> list:
    """
    Calculates counts of each spam phrase found in email message.

    Args:
        email_message (str): Email message text.
        spam_phrases (list): List of phrases to search for.

    Returns:
        list
    """
    #   List containing found phrases and their count.
    spam_phrases_found = []
    #   Convert email message to lowercase so search is not case sensitive.
    email_message_lower = email_message.lower()
    #   Iterate through each spam phrase.
    for spam_phrase in spam_phrases:
        #   Convert spam_phrase to lowercase so search is not case sensitive.
        spam_phrase_lower = spam_phrase.lower()
        #   Determine if the spam phrase is found in the email message.
        spam_phrase_count = email_message_lower.count(spam_phrase_lower)
        if spam_phrase_count > 0:
            #   Spam phrase found. Add the phrase and the number of
            #   occurrences to the spam phrases found list.
            spam_phrases_found.append([spam_phrase_lower, spam_phrase_count])

    return spam_phrases_found

if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass