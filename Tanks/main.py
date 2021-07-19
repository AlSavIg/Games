from Packages.rendering import render
from Packages.control import control_signal
from Packages.field_creating import create_field, tank_pos
from Packages.clear_console import clear_console


# print(help(render))
# print(help(control_signal))
# print(help(tank_pos))
# print(help(create_field))
# print(help(clear_console))
# print(help(start_game))


def start_game() -> None:
    """
        Позволяет собрать все функции всех модулей воедино и начать игру.
    """
    game_field = create_field()

    while True:
        render(game_field)
        print('\n')
        player_turn = control_signal()
        game_field = tank_pos(game_field, player_turn)
        clear_console()
        if player_turn == 'q':
            print('GAME OVER')
            break


start_game()
