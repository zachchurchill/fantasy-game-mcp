import random
from typing import Tuple


def roll_dice(*, num_sides: int, num_dice: int) -> Tuple[int, ...]:
    return tuple(random.randint(1, num_sides) for _ in range(num_dice))