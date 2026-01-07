import random
from typing import Tuple


def roll_dice(*, num_sides: int, num_dice: int) -> Tuple[int, ...]:
    if num_sides <= 0:
        raise ValueError(f"Number of sides must be greater than 0, got {num_sides}")
    if num_dice <= 0:
        raise ValueError(f"Number of dice must be greater than 0, got {num_dice}")

    return tuple(random.randint(1, num_sides) for _ in range(num_dice))