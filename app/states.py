from aiogram.fsm.state import StatesGroup, State


class RegStates(StatesGroup):
    reg_first = State()
    choose_device = State()
