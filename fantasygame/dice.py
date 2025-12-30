import random
from typing import Tuple


def _roll_dice(num_dice: int, num_sides: int) -> Tuple[int, ...]:
    return tuple(random.randint(1, num_sides) for _ in range(num_dice))


def roll_d6(num_dice=1) -> Tuple[int, ...]:
    return _roll_dice(num_dice, 6)


def roll_d20(num_dice=1) -> Tuple[int, ...]:
    return _roll_dice(num_dice, 20)
