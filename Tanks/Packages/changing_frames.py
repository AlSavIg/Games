from .field_creating import create_field
import os
# from .control import control_signal
# from field_creating import create_field


ACCEPTABLE_MOVES = {'straight': 'w',
                    'left': 'a',
                    'back': 's',
                    'right': 'd'}
# Doesn't depend on the current 'head' position
CURRENT_HEAD_POS = {'i': 1,
                    'j': 3,
                    'eyeliner': 'd'}
# i, j or y, x (according to school program)


def tank_move(playing_field: tuple, player_turn: str) -> tuple:
    """
        Принимает на вход текущее состояние игрового поля, а также ход игрока,
        после чего вносит в игровое поле изменения в соответствии со сделанным ходом,
        возвращая в итоге новое, измененное состояние игрового поля для отрисовки (вывода).
    """
    global CURRENT_HEAD_POS
    field_len = len(playing_field[0])
    field_wid = len(playing_field)
    if player_turn == ACCEPTABLE_MOVES['straight']:
        if CURRENT_HEAD_POS['eyeliner'] == ACCEPTABLE_MOVES['straight']:
            CURRENT_HEAD_POS['i'] -= 1
            playing_field = create_field(field_len,
                                         field_wid,
                                         (CURRENT_HEAD_POS['i'], CURRENT_HEAD_POS['j']))
    elif player_turn == ACCEPTABLE_MOVES['left']:
        if CURRENT_HEAD_POS['eyeliner'] == ACCEPTABLE_MOVES['left']:
            CURRENT_HEAD_POS['j'] -= 1
            playing_field = create_field(field_len,
                                         field_wid,
                                         (CURRENT_HEAD_POS['i'], CURRENT_HEAD_POS['j']))
    elif player_turn == ACCEPTABLE_MOVES['back']:
        if CURRENT_HEAD_POS['eyeliner'] == ACCEPTABLE_MOVES['back']:
            CURRENT_HEAD_POS['i'] += 1
            playing_field = create_field(field_len,
                                         field_wid,
                                         (CURRENT_HEAD_POS['i'], CURRENT_HEAD_POS['j']))
    elif player_turn == ACCEPTABLE_MOVES['right']:
        if CURRENT_HEAD_POS['eyeliner'] == ACCEPTABLE_MOVES['right']:
            CURRENT_HEAD_POS['j'] += 1
            playing_field = create_field(field_len,
                                         field_wid,
                                         (CURRENT_HEAD_POS['i'], CURRENT_HEAD_POS['j']))
    # else:
    #     print('WRONG TURN')

    return playing_field


def clear_window() -> None:
    """
        Очищает окно для начала отрисовки следующего кадра.
    """
    os.system('cls')
