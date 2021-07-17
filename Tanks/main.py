from Packages.rendering import render
from Packages.control import control_signal
from Packages.changing_frames import tank_move, clear_window
from Packages.field_creating import create_field


# print(help(render))
# print(help(control_signal))
# print(help(tank_move))
# print(help(create_field))
# print(help(clear_window))
# print(help(start_game))


def start_game() -> None:
    """
        Позволяет собрать все функции всех модулей воедино и начать игру.
    """
    game_field = create_field()
    player_turn = ''

    while player_turn != 'q':
        render(game_field)
        print('\n')
        player_turn = control_signal()
        game_field = tank_move(game_field, player_turn)
        clear_window()


start_game()
