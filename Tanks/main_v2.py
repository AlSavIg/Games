from Control.pynput_control import start_read
from Packages.menu_v2 import print_menu

# print(help(start_read))
# print(help(print_menu))


def start_game() -> None:
    """
        Позволяет собрать все функции всех модулей воедино и начать игру.
    """
    print_menu()
    start_read()


start_game()
