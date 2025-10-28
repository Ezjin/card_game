from card_game.card import Card

class Deck:
    """
    Representa um deck de cartas de baralho

    Attributes:
    Game: Para qual jogo o deck de cartas sera usado (Scoundrel)
    """

    GAMES = ["Scoundrel"]
    CARDS = {
        "Scoundrel":
        [
            Card("K", "Clubs"),
            Card("Q", "Clubs"),
            Card("J", "Clubs"),
            Card("10", "Clubs"),
            Card("9", "Clubs"),
            Card("8", "Clubs"),
            Card("7", "Clubs"),
            Card("6", "Clubs"),
            Card("5", "Clubs"),
            Card("4", "Clubs"),
            Card("3", "Clubs"),
            Card("2", "Clubs"),
            Card("A", "Clubs"),

            Card("K", "Spades"),
            Card("Q", "Spades"),
            Card("J", "Spades"),
            Card("10", "Spades"),
            Card("9", "Spades"),
            Card("8", "Spades"),
            Card("7", "Spades"),
            Card("6", "Spades"),
            Card("5", "Spades"),
            Card("4", "Spades"),
            Card("3", "Spades"),
            Card("2", "Spades"),
            Card("A", "Spades"),

            Card("10", "Hearts"),
            Card("9", "Hearts"),
            Card("8", "Hearts"),
            Card("7", "Hearts"),
            Card("6", "Hearts"),
            Card("5", "Hearts"),
            Card("4", "Hearts"),
            Card("3", "Hearts"),
            Card("2", "Hearts"),
            Card("A", "Hearts"),

            Card("10", "Diamonds"),
            Card("9", "Diamonds"),
            Card("8", "Diamonds"),
            Card("7", "Diamonds"),
            Card("6", "Diamonds"),
            Card("5", "Diamonds"),
            Card("4", "Diamonds"),
            Card("3", "Diamonds"),
            Card("2", "Diamonds"),
            Card("A", "Diamonds"),
        ]
    }

    def __init__ (self, game):
        if game not in self.GAMES:
            raise ValueError(f"Invalid game: {game}")
        self._deck = self.CARDS[game]
        
    def buy(self):
        if not self.deck:
            return None    
        return self.deck.pop()
        