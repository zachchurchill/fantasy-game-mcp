import random
from unittest.mock import patch, Mock

import pytest
from mcp import Tool

from main import mcp


@pytest.mark.asyncio
async def test_tools_registered():
    tools = await mcp.list_tools()

    expected_tools = [
        "roll_d6",
        "roll_d20",
        "get_character_classes",
    ]
    assert len(tools) == len(expected_tools)
    assert set([tool.name for tool in tools]) == set(expected_tools)

@pytest.mark.asyncio
@pytest.mark.parametrize("i", range(20))
async def test_roll_d6(i):
    num_dice = random.randint(1, 100)

    _, result_response = await mcp.call_tool("roll_d6", {"num_dice": num_dice})

    assert "result" in result_response
    result = result_response["result"]
    assert len(result) == num_dice
    assert all(1 <= die <= 6 for die in result)

@pytest.mark.asyncio
@pytest.mark.parametrize("i", range(20))
async def test_roll_d20(i):
    num_dice = random.randint(1, 100)

    _, result_response = await mcp.call_tool("roll_d20", {"num_dice": num_dice})

    assert "result" in result_response
    result = result_response["result"]
    assert len(result) == num_dice
    assert all(1 <= die <= 20 for die in result)

@pytest.mark.asyncio
async def test_get_character_classes():
    with patch("fantasygame.character.requests.get") as mock_get:
        mock_get.return_value = Mock(status_code=200, json=lambda: {"results": [{"name": "Barbarian"}, {"name": "Bard"}]})

        _, result_response = await mcp.call_tool("get_character_classes", {})

        assert "result" in result_response
        result = result_response["result"]
        assert result == ["Barbarian", "Bard"]