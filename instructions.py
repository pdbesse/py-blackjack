class Card:

    # Card constructor
    # The suit and value of a card, should be immutable.
    def __init__(self, suit: str, value: str):
        pass
    # Returns the suit of the card.
    def suit(self) -> str:
       pass
    # Returns the value of the card.
    def value(self) -> str:
        pass     
    # Returns a string representation of Card
    # E.g. "Ace of Spades"
    def __str__(self) -> str:
        pass

class Deck:
    
    # Creates a sorted deck of playing cards. 13 values, 4 suits.
    # You will iterate over all pairs of suits and values to add them to the deck.
    # Once the deck is initialized, you should prepare it by shuffling it once.
    def __init__(self):
      SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
      VALUES = ["Ace", "Two" , "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
      
      
    
    # Returns the number of Cards in the Deck
    def size(self) -> int:
        pass
    # Shuffles the deck of cards. This means randomzing the order of the cards in the Deck.
    def shuffle(self) -> None:
        pass
    # Returns the top Card in the deck, but does not modify the deck.
    def peek(self) -> Card:
        pass
    # Removes and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self) -> Card:
        pass
    # Adds the input card to the deck. 
    # If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self, card: Card) -> None:
        pass
    # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self) -> None:
        pass
    # Resets the deck to it's original state with all 52 cards.
    # Also shuffle the deck.
    def reset(self) -> None:
        pass
    
class Blackjack:
  # Creates a Blackjack game with a new Deck.
  def __init__(self):
        pass  
  # Computes the score of a hand. 
  # For examples of hands and scores as a number.
  # 2,5 -> 7
  # 3, 10 -> 13
  # 5, King -> 15
  # 10, Ace -> 21
  # 10, 8, 4 -> Bust so return -1
  # 9, Jack, Ace -> 20 
  # If the Hand is a bust return -1 (because it always loses)
  def _get_score(self, hand: List[Card]) -> int:
        pass
  
  # Prints the current hand and score.
  # E.g. would print out (Ace of Clubs, Jack of Spades, 21)
  # E.g. (Jack of Clubs, 5 of Diamonds, 8 of Hearts, "Bust!")
  def _print_current_hand(self) -> None:
        pass
  
  # The previous hand is discarded and shuffled back into the deck.
  # Should remove the top 2 cards from the current deck and 
  # Set those 2 cards as the "current hand". 
  # It should also print the current hand and score of that hand.
  # If less than 2 cards are in the deck, 
  # then print an error instructing the client to shuffle the deck.
  def deal_new_hand(self) -> None:
        pass
  # Deals one more card to the current hand and prints the hand and score.
  # If no cards remain in the deck, print an error.
  def hit(self) -> None: 
        pass
  
  # Reshuffles all cards in the "current hand" and "discard pile"
  # and shuffles everything back into the Deck.
  def reshuffle(self) -> None:
        pass