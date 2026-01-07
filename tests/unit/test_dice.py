from unittest.mock import patch

import pytest

from fantasygame.dice import roll_dice


@pytest.fixture
def mock_random_randint():
    with patch("fantasygame.dice.random.randint") as mock_randint:
        mock_randint.return_value = 1
        yield mock_randint

def test_single_dice_roll(mock_random_randint):
    result = roll_dice(num_sides=6, num_dice=1)
    assert result == (1,)

def test_multiple_dice_roll(mock_random_randint):
    result = roll_dice(num_sides=6, num_dice=3)
    assert len(result) == 3
    assert sum(result) == 3

def test_roll_dice_range():
    result = roll_dice(num_sides=6, num_dice=50)
    assert all(1 <= die <= 6 for die in result)

def test_invalid_num_sides(mock_random_randint):
    with pytest.raises(ValueError):
        roll_dice(num_sides=0, num_dice=1)

def test_invalid_num_dice(mock_random_randint):
    with pytest.raises(ValueError):
        roll_dice(num_sides=6, num_dice=0)