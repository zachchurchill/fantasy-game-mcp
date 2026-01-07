from typing import List, Tuple

from mcp.server.fastmcp import FastMCP

from fantasygame.dice import roll_dice
from fantasygame.character import Character


mcp = FastMCP("DullFantasyGame", json_response=True)


@mcp.tool()
def roll_d6(num_dice: int = 1) -> Tuple[int, ...]:
    return roll_dice(num_sides=6, num_dice=num_dice)


@mcp.tool()
def roll_d20(num_dice: int = 1) -> Tuple[int, ...]:
    return roll_dice(num_sides=20, num_dice=num_dice)


@mcp.tool()
def get_character_classes() -> List[str]:
    """Returns same character classes as DnD API provides."""
    return Character.get_available_jobs()


@mcp.resource("introduction://{name}")
def get_game_introduction(name: str) -> str:
    return f"Greetings {name}, I am the game master for this dull fantasy game."


if __name__ == "__main__":
    mcp.run()
