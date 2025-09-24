


class Card():
    allowed_suits = {"hearts", "diamonds", "clubs", "spades"}        
    suit_dict = {
                "hearts":"♥",
                "diamonds":"♦",
                "clubs":"♣",
                "spades":"♠"
                }
    def __init__ (self, rank, suit):
        if suit.lower() not in self.allowed_suits:
            raise ValueError(f"Invalid suit: {suit}. It should be one of those {self.allowed_suits}") 
        self.rank = rank
        self.suit = self.suit_dict[suit.lower()]

    def render(self):
        size_line = 10
        size_line_rank = size_line - len(self.rank) 
        size_line_suit = size_line - len(self.suit)
        
        return [
                " " + "_" * (size_line) + ".",
                f"|{self.rank}" + " " * size_line_rank + "|",
                f"|{self.suit}" + " " * size_line_suit + "|",
                "|" + " " * size_line + "|",
                "|" + " " * size_line + "|",
                "|" + " " * size_line + "|",
                "|" + " " * size_line_suit + f"{self.suit}|",
                #"|" + " " * size_line_rank+ f"{self.rank}|",
                "|" + "_" * size_line_rank + f"{self.rank}|"
        ]

    def show(self):
        for line in self.render():
            print(line)

def print_cards(cards):
    for lines in zip(*(c.render() for c in cards)):
        print(" ".join(lines))

c1 = Card("A", "spades")
c2 = Card("K", "hearts")
c3 = Card("9", "diamonds")

cards = [c1, c2, c3]

print_cards(cards)

c1.show()


