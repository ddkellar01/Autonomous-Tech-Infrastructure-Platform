import pytest
from src.scout_bot.scout_bot import TechScoutBot

def test_scout_initialization():
    bot = TechScoutBot()
    assert bot is not None
    assert isinstance(bot.headers, dict)
