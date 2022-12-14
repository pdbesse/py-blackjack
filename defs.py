import random
from typing import List

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
        return f"{self.value + ' of ' + self.suit}"

class Deck:
    
    # Creates a sorted deck of playing cards. 13 values, 4 suits.
    # You will iterate over all pairs of suits and values to add them to the deck.
    # Once the deck is initialized, you should prepare it by shuffling it once.
    def __init__(self):
      SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
      VALUES = ["Ace", "Two" , "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
      
      self.deck = []
      for suit in SUITS:
        for value in VALUES:
            card = Card(suit, value)
            self.deck.append(card)
      self.shuffle()
    
    # Returns the number of Cards in the Deck
    def size(self) -> int:
        print(len(self.deck))

    # Shuffles the deck of cards. This means randomzing the order of the cards in the Deck.
    def shuffle(self) -> None:
        random.shuffle(self.deck)

    # Returns the top Card in the deck, but does not modify the deck.
    def peek(self) -> Card:
        print(self.deck[-1])

    # Removes and returns the top card in the deck. The card should no longer be in the Deck.
    def draw(self) -> Card:
        return self.deck.pop()

    # Adds the input card to the deck. 
    # If the deck has more than 52 cards, do not add the card and raise an exception.
    def add_card(self, card: Card) -> None:
        if len(self.deck) < 53:
            self.deck.append(card)
        else:
            raise Exception("Deck is full")

    # Calling this function should print all the cards in the deck in their current order.
    def print_deck(self) -> None:
        for i in range(len(self.deck)):
            print(self.deck[i])

    # Resets the deck to it's original state with all 52 cards.
    # Also shuffle the deck.
    def reset(self) -> None:
        self.__init__()
        self.shuffle()

class Blackjack:
  # Creates a Blackjack game with a new Deck.
  def __init__(self):
        deck = Deck() 

  # Computes the score of a hand. 
  # For examples of hands and scores as a number.
  # 2,5 -> 7
  # 3, 10 -> 13
  # 5, King -> 15
  # 10, Ace -> 21
  # 10, 8, 4 -> Bust so return -1
  # 9, Jack, Ace -> 20 
  # If the Hand is a bust return -1 (because it always loses)
  def _get_score(self) -> int:
    # init score and num_aces variables
    score = 0
    num_aces = 0
    card_value = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10}
    
    # compile number of aces
    # for card in self.hand:
    #     if (card.value == "Ace"): num_aces += 1
    
    # for card in self.hand:
    #     if (card.value != "Ace"):
    #         score += card_value[card.value]

    # sum the face value of the cards in the hand
    for card in self.hand:
        # print(card)
        if card.value == "Ace":
            score += 11
            num_aces += 1
        elif card.value == "Jack" or "Queen" or "King":
            score += 10
        else:
            score += card_value[card.value]
    
    # handle aces
    while score > 21 and num_aces > 0:
      score -= 10
      num_aces -= 1
    
    # return the score or -1 if the hand is a bust
    if score > 21:
      return -1
    else:
      return score

  
  # Prints the current hand and score.
  # E.g. would print out (Ace of Clubs, Jack of Spades, 21)
  # E.g. (Jack of Clubs, 5 of Diamonds, 8 of Hearts, "Bust!")
  def _print_current_hand(self) -> None:
        current_hand_str = []
        for card in self.hand:
            current_hand_str.append(card.__str__)

        score = self._get_score(self.hand)
        print("Current Hand: ", current_hand_str, score)
  
  # The previous hand is discarded and shuffled back into the deck.
  # Should remove the top 2 cards from the current deck and 
  # Set those 2 cards as the "current hand". 
  # It should also print the current hand and score of that hand.
  # If less than 2 cards are in the deck, 
  # then print an error instructing the client to shuffle the deck.
  def deal_new_hand(self) -> None:
    if len(self.deck) < 2:
      print("Please shuffle the deck.")

  # Deals one more card to the current hand and prints the hand and score.
  # If no cards remain in the deck, print an error.
  def hit(self) -> None: 
        if (len(self.deck) == 0): print("error")
        else:
            self.hand.append(self.deck.draw())
            self._print_current_hand()
  
  # Reshuffles all cards in the "current hand" and "discard pile"
  # and shuffles everything back into the Deck.
  def reshuffle(self) -> None:
        pass