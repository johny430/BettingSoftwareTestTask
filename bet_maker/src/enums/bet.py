from enum import Enum


class BetStatus(int, Enum):
    PENDING = 1
    WIN = 2
    LOSE = 3
