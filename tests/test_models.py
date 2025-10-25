import pytest
from card_game.card import Card


def test_suit_error():
    with pytest.raises(ValueError) as excinfo:
        Card("A", "bananas")
    assert str(excinfo.value) == "Invalid suit: bananas"

def test_rank_error():
    with pytest.raises(ValueError) as excinfo:
        Card(14, "Diamonds")
    assert str(excinfo.value) == "Invalid rank: 14"

def test_print_success():
    c = Card("A", "Hearts")
    assert str(c) == "A of Hearts ♥"

def test_repr():
    c = Card("A", "Hearts")
    assert repr(c) == "Card(Rank = A, Suit = Hearts)"

@pytest.mark.parametrize("rank, value", [
("A", 1),
("2", 2),
("J", 11),
("K", 13),
])
def test_value_mapping(rank, value):
    assert Card(rank, "Diamonds").value == value