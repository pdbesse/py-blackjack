class Card:

    # Card constructor
    # The suit and value of a card, should be immutable.
    def __init__(self, suit: str, value: str):

        # Suit of card
        self.suit = suit
        # Value of card
        self.value = value

    # Returns the suit of the card.
    def suit(self) -> str:
        return self.suit

    # Returns the value of the card.
    def value(self) -> str:
        return self.value

    # Returns a string representation of Card
    # E.g. "Ace of Spades"
    def __str__(self) -> str:
        return self.value + 'of' + self.suit
