class Card:
    """
    Representa uma carta de baralho.
    
    Attributes:
        SUITS: Available (hearts, diamonds, clubs, spades)
        RANKS: Available ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        SYMBOLS: Unicode for each Suit.

    """
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    SYMBOLS = {"Hearts": "♥", "Diamonds": "♦", "Clubs": "♣", "Spades": "♠"}
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    VALUES = {rank: i + 1 for i, rank in enumerate(RANKS)}

    def __init__(self, rank, suit):
        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        self._rank = rank
        self._suit = suit
        self._symbol = self.SYMBOLS[suit]

    @property
    def rank(self):
        return self._rank
    
    @property
    def suit(self):
        return self._suit
    
    @property
    def value(self):
        return self.VALUES[self._rank]
    
    def __str__(self):
        return f"{self._rank} of {self._suit} {self._symbol}"
    
    def __repr__(self):
        return f"Card(Rank = {self._rank}, Suit = {self._suit})"

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self._rank == other._rank and self._suit == other._suit
    
    
