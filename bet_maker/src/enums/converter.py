from src.enums.bet import BetState
from src.enums.event import EventState


def get_bet_status_base_on_event_state(event_status: EventState):
    if event_status == EventState.FINISHED_WIN:
        return BetState.WIN
    elif event_status.FINISHED_LOSE:
        return BetState.LOSE
    return BetState.PENDING
