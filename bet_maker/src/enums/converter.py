from src.enums.bet import BetStatus
from src.enums.event import EventStatus


def get_bet_status_based_on_event_status(event_status: EventStatus):
    if event_status == EventStatus.FINISHED_WIN:
        return BetStatus.WIN
    elif event_status.FINISHED_LOSE:
        return BetStatus.LOSE
    return BetStatus.PENDING
