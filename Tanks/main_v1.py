from Packages.rendering import render
from Tanks.Control.input_control import control_signal
from Packages.field_creating import create_field
from Packages.clear_console import clear_console
from Packages.constants import FIELD_SIZE
from Packages.menu_v1 import show_menu

# print(help(render))
# print(help(control_signal))
# print(help(create_field))
# print(help(clear_console))
# print(help(start_game))
# print(help(show_menu))


def start_game() -> None:
    """
        Позволяет собрать все функции всех модулей воедино и начать игру.
    """
    player_turn = show_menu()
    clear_console()
    game_field = create_field(player_turn, *FIELD_SIZE)
    render(game_field)
    while True:
        player_turn = control_signal()
        if player_turn == 'q':
            clear_console()
            print('GAME OVER')
            break
        clear_console()
        game_field = create_field(player_turn, *FIELD_SIZE)
        render(game_field)


start_game()
