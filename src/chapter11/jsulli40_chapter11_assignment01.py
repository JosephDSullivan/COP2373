#!/usr/bin/env python3
"""
tbd

Author
    Joseph D Sullivan <JSulli40@Student.SCF.edu>

Date
    April 13, 2025

Chapter
    11

Assignment
    01

Repository
    https://github.com/JosephDSullivan/COP2373/blob/main/src/chapter11/jsulli40_chapter11_assignment01.py

Problem Description
    Using the Deck object presented in Section 11.5, write a game program that
    deals a Poker hand of five cards. Then prompt the user to enter a series
    of numbers (for example: 1, 3, 5) that selects cards to be replaced during
    a draw phrase. Then print the result of drawing the new cards.
    You should have at least two functions, but you can have more.
    Submit your .py file in this assignment and in your repository.
    You DO NOT NEED a technical design document for this assignment.
"""

import random


def main():
    """
    Entry function for when code is invoked directly.
    """
    #   Generate and display original hand.
    deck = Deck()
    hand = Hand(deck)
    print(f"\nOriginal Hand:")
    print(f"\t\t{hand}")

    #   Retrieve list of positions to draw.
    input_draw = input(f"\nEnter positions to discard and draw "
                       f"(1-{hand.CARDS_PER_HAND}) (e.g. 1 3 4): ")
    #   Validate draw position list.
    draw_list = input_draw.split()
    draw_list_int = [int(pos) for pos in draw_list]
    for pos in draw_list_int:
        if pos < 1:
            raise ValueError(f"Position ({pos}) must be greater than 0.")
        if pos > hand.CARDS_PER_HAND:
            raise ValueError(f"Position ({pos}) must be less than or equal " +
                             f"to the number of cards in hand "
                             f"({hand.CARDS_PER_HAND}).")

    #   Draw cards at appropriate positions. Notify user.
    hand.draw(draw_list_int)
    print("\nDrawing Cards...\n")

    #   display final hand.
    print(f"Final Hand:")
    print(f"\t\t{hand}")


class Deck:
    """
    Deck of playing cards. Initialize with shuffling, dealing cards, and
    discarding cards.
    """

    def __init__(self, num_decks: int = 1):
        """
        Initialize deck.

        Args:
            num_decks (int): Number of card decks to use.
        """
        #   Validate num_decks.
        num_decks = int(num_decks)
        if num_decks < 1:
            raise ValueError("Number of decks must be at least 1.")
        #   Populate deck and shuffle it.
        self.deck = [f"{num} {suit}"
                     for suit in "\u2665\u2666\u2663\u2660"
                     for num in "A23456789TJQK"
                     for _ in range(num_decks)]
        random.shuffle(self.deck)
        #   Initialize other variables.
        self.cards_in_play = []
        self.cards_discarded = []

    def deal_card(self) -> str:
        """
        Deal a card from end of deck. If no cards exist in deck, then shuffle
        cards_discarded into deck.

        Returns:
            str: The dealt card.
        """
        #   Verify there is at least one card to deal in deck.
        if not self.deck:
            #   Verify that there is at least one card in the discarded list.
            #   If not, raise error.
            if not self.cards_discarded:
                raise ValueError("No cards to deal.")
            #   Reshuffle discarded list into deck.
            print(f"Deck reshuffling...")
            random.shuffle(self.cards_discarded)
            self.deck = self.cards_discarded
            self.cards_discarded.clear()
        #   Deal the last card in the deck and return it.
        new_card = self.deck.pop()
        self.cards_in_play.append(new_card)
        return new_card

    def discard_cards_in_play(self):
        """
        Transfer cards_in_play into cards_discarded.
        """
        self.cards_discarded.extend(self.cards_in_play)
        self.cards_in_play.clear()


class Hand:
    """
    Hand of poker.
    """

    CARDS_PER_HAND: int = 5

    def __init__(self, deck: Deck):
        """
        Initialize hand with cards drawn from specified deck.

        Args:
            deck (Deck): The specified deck.
        """
        self.deck = deck
        self.cards = [self.deck.deal_card() for _ in
                      range(self.CARDS_PER_HAND)]

    def __str__(self) -> str:
        """
        String representation of the current hand.

        Returns:
            str: Cards in hand, numbered from 1 to CARDS_PER_HAND.
        """
        return "\t\t".join(f"{card_num + 1}: {card}"
                           for card_num, card in enumerate(self.cards))

    def draw(self, indices: list[int] = None):
        """
        Discard and redraw cards at the specified indices.

        Args:
            indices (list[int], optional): A permutation of 1-based indices of cards to replace.
                                           If None or empty, nothing is changed.

        Raises:
            ValueError: If indices are invalid (e.g., duplicates, out-of-range, wrong count).
        """
        if indices is None:
            return

        # Validate indices: must be integers in 1..CARDS_PER_HAND with no duplicates
        if (not all(isinstance(i, int) for i in indices)
                or sorted(indices) != sorted(set(indices))
                or not all(1 <= i <= self.CARDS_PER_HAND for i in indices)):
            raise ValueError(
                f"indices must be unique integers in range [1, {self.CARDS_PER_HAND}]"
            )

        for i in indices:
            # Convert 1-based to 0-based index
            self.deck.cards_discarded.append(self.cards[i - 1])
            self.cards[i - 1] = self.deck.deal_card()


if __name__ == "__main__":
    #   Execute this code when invoked directly.
    main()
else:
    #   Execute this code when imported.
    pass
