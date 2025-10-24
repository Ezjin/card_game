import pytest
from card_game.models import Card

def test_suit_error():
    with pytest.raises(ValueError) as excinfo:
        Card("A", "bananas")
    assert str(excinfo.value) == "Invalid suit: bananas"

def test_rank_error():
    with pytest.raises(ValueError) as excinfo:
        Card(14, "diamonds")
    assert str(excinfo.value) == "Invalid rank: 14"
