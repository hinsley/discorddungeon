import enum
from dataclasses import dataclass
from typing import List

class Setting(enum.Enum):
    FANTASY     = enum.auto()
    MYSTERY     = enum.auto()
    APOCALYPTIC = enum.auto()
    ZOMBIES     = enum.auto()
    CYBERPUNK   = enum.auto()
    TIGER_KING  = enum.auto()
    QUARANTINE  = enum.auto()
    CUSTOM      = enum.auto()

@dataclass
class StoryChunk():
    """ A piece of history from the established story in a particular game. """
    player_generated : bool
    content          : str

@dataclass
class Game():
    """ A game's state. """
    player_name : str
    history     : List[StoryChunk]
    setting     : Setting = Setting.FANTASY
