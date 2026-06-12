from aiogram.fsm.state import State, StatesGroup

class ReportForm(StatesGroup):
    waiting_for_example = State()

