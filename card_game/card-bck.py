class Card:
    SUITS = ["hearts", "diamonds", "clubs", "spades"]
    SUITS_SYMBOLS = {"hearts": "♥", "diamonds": "♦", "clubs": "♣", "spades": "♠"}
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, rank, suit, flip=True):
        if suit.lower() not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        self.rank = rank
        self.suit = suit
        self.flip = flip
        self.simbol = self.SUITS_SYMBOLS[suit.lower()]

    def __str__(self):
        return f"{self.rank} of {self.suit} {self.simbol}"
    
    def __repr__(self):
        return f"Card(Rank = {self.rank}, Suit = {self.suit})"

    def render(self):
        size_line = 10
        size_line_rank = size_line - len(self.rank)
        size_line_suit = size_line - len(self.suit)

        if self.flip:
            return [
                " " + "_" * (size_line) + ".",
                f"|{self.rank}" + " " * size_line_rank + "|",
                f"|{self.suit}" + " " * size_line_suit + "|",
                "|" + " " * size_line + "|",
                "|" + " " * size_line + "|",
                "|" + " " * size_line + "|",
                "|" + " " * size_line_suit + f"{self.suit}|",
                # "|" + " " * size_line_rank+ f"{self.rank}|",
                "|" + "_" * size_line_rank + f"{self.rank}|",
            ]
        else:
            return [
                " " + "_" * (size_line) + ".",
                "|\\" + " " * (size_line - 2) + "/|",
                "| \\" + " " * (size_line - 4) + "/ |",
                "|  \\" + " " * (size_line - 6) + "/  |",
                "|" + " " * (size_line - 6) + "CG" + " " * (size_line - 6) + "|",
                "|  /" + " " * (size_line - 6) + "\\  |",
                "| /" + " " * (size_line - 4) + "\\ |",
                "|/" + "_" * (size_line - 2) + "\\|",
            ]

    def show(self):
        for line in self.render():
            print(line)
