import pytest
from card_game.models import Card

def test_create_card_error():
    with pytest.raises(ValueError) as excinfo:
        Card("A", "bananas")
    assert str(excinfo.value) == "Invalid suit: bananas. It should be one of those ['hearts', 'diamonds', 'clubs', 'spades']"
