import pytest
from card_game.deck import Deck

def test_game_error():
    with pytest.raises(ValueError) as excinfo:
        d = Deck("Poker")
    assert str(excinfo.value) == "Invalid game: Poker"