from Packages.rendering import render
from Packages.control import control_signal
from Packages.changing_frames import tank_move
from Packages.field_creating import create_field


# print(help(render))
# print(help(control_signal))
# print(help(tank_move))
# print(help(create_field))


def start_game() -> None:
    """
        Позволяет собрать все функции всех модулей воедино и начать игру
    """
