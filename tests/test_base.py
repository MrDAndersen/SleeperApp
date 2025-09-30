import pytest
from sleeper.base import SleeperBase

@pytest.fixture
def sleeper_base():
    # Initialize with sport = "nfl"
    return SleeperBase("nfl")

def test_state_scroll_is_dict(sleeper_base):
    """
    🧭 Validates that the state scroll is a dictionary.
    """
    assert isinstance(sleeper_base.state, dict), "State scroll should be a dict"

def test_player_registry_not_empty(sleeper_base):
    """
    🧙 Ensures player registry returns data.
    """
    players = sleeper_base.get_players()
    assert isinstance(players, dict), "Player registry should be a dict"
    assert len(players) > 0, "Player registry should not be empty"

def test_trending_scroll_has_expected_keys(sleeper_base):
    """
    🔮 Validates trending scroll structure.
    """
    trending = sleeper_base.get_trending_players(type="add")
    assert isinstance(trending, dict), "Trending scroll should be a dict"
    assert "data" in trending and "headers" in trending, "Trending scroll should include data and headers"
    assert isinstance(trending["data"], list), "Trending data should be a list"
