class Card():
    SUITS = ["hearts", "diamonds", "clubs", "spades"]        
    suit_dict = {
                "hearts":"♥",
                "diamonds":"♦",
                "clubs":"♣",
                "spades":"♠"
                }
    def __init__ (self, rank, suit, flip = True):
        if suit.lower() not in self.SUITS:
            raise ValueError(f"Invalid suit: {suit}.")
        self.rank = rank
        self.suit = self.suit_dict[suit.lower()]
        self.flip = flip

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
                    #"|" + " " * size_line_rank+ f"{self.rank}|",
                    "|" + "_" * size_line_rank + f"{self.rank}|"
            ]
        else:
            return [
                " " + "_" * (size_line) + ".",
                "|\\" + " " * (size_line - 2) + "/|",
                "| \\" + " " * (size_line - 4) + "/ |",
                "|  \\" + " " * (size_line - 6) + "/  |",
                "|" + " " * (size_line - 6) + "CG" +  " " * (size_line - 6) + "|",
                "|  /" + " " * (size_line - 6) + "\\  |",
                "| /" + " " * (size_line - 4) + "\\ |",
                "|/" + "_" * (size_line - 2) + "\\|"
            ]
            
    def show(self):
        for line in self.render():
            print(line)

def print_cards(cards):
    for lines in zip(*(c.render() for c in cards)):
        print(" ".join(lines))

c1 = Card("A", "spades")
c2 = Card("K", "hearts", False)
c3 = Card("10", "diamonds")

cards = [c1, c2, c3]

print_cards(cards)

c1.show()


