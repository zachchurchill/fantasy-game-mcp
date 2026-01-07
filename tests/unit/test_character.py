from unittest.mock import patch, Mock

import pytest

from fantasygame.character import Character


@pytest.fixture
def mock_requests_get():
    with patch("fantasygame.character.requests.get") as mock_get:
        mock_get.return_value = Mock(status_code=200, json=lambda: {"results": [{"name": "Barbarian"}]})
        yield mock_get

def test_get_available_jobs(mock_requests_get):
    jobs = Character.get_available_jobs()
    assert jobs == ["Barbarian"]

def test_get_available_jobs_error(mock_requests_get):
    mock_requests_get.return_value = Mock(status_code=500)
    jobs = Character.get_available_jobs()
    assert jobs == []