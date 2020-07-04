from dataclasses import dataclass
from enum import Enum
from typing import List

class Setting(Enum):
    FANTASY = 1
    MYSTERY = 2
    APOCALYPTIC = 3
    ZOMBIES = 4
    CYBERPUNK = 5
    TIGER_KING = 6
    QUARANTINE = 7
    CUSTOM = 8

@dataclass
class StoryChunk():
    """ A piece of history from the established story in a particular game. """
    player_generated: bool
    content: str

@dataclass
class Game():
    """ A game's state. """
    player_name: str
    history: List[StoryChunk]
    setting: Setting = Setting.FANTASY
