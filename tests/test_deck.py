import pytest
from card_game.deck import Deck

def test_game_error():
    with pytest.raises(ValueError) as excinfo:
        d = Deck("Poker")
    assert str(excinfo.value) == "Invalid game: Poker"

def test_buy_empty():
    deck = Deck("Empty")
    assert not deck.buy()

def test_buy_non_empty():
    deck = Deck("Scoundrel")
    c = deck.buy()
    assert str(c) == "K of Clubs ♣"
   
    
def test_return_card():
    deck = Deck("Scoundrel")
    c = deck.buy()
    deck.return_bottom(c)
    assert c == deck._deck.pop()

def test_return_other():
    with pytest.raises(TypeError) as excinfo:
        deck = Deck("Empty")
        deck.return_bottom("As de Espadas")
    assert str(excinfo.value) == "Expected a Card Object" 

def test_restart():
    deck = Deck("Scoundrel")
    deck.buy()
    deck.restart()
    assert deck.size == 46