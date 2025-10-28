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

    @property
    def symbol(self):
        return self.SYMBOLS[self._suit]

    def __str__(self):
        return f"{self._rank} of {self._symbol} {self._suit}"

    def __repr__(self):
        return f"Card(Rank = {self._rank}, Suit = {self._suit})"

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self._rank == other._rank and self._suit == other._suit

    def __sub__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.value - other.value

if __name__ == "__main__":
    c1 = Card("K", "Diamonds")
    c2 = Card("6", "Spades")
    print(f"Suit: {c1.suit}.")
    print(f"Symbol: {c1.symbol}.")
    print(f"Rank: {c1.rank}")
    print(f"Value: {c1.value}")
    print(f"{c1} - {c2} = {c1 - c2} in value")
