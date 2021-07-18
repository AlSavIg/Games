import os
from .field_creating import create_field
from .constants import START_HEAD_POS, DIRECTIONS
# from .control import control_signal
# from field_creating import create_field

current_head_pos = START_HEAD_POS.copy()


def head_move(player_turn: str, head_pos: dict) -> dict:
    """
        Принимает на вход ход игрока и текущее положение 'дула' ('head') танка.
        Возвращает новое положение 'дула' ('head') танка.
    """
    if player_turn == DIRECTIONS['straight']:
        if head_pos['eye_direct'] == DIRECTIONS['straight']:
            head_pos['i'] -= 1
    elif player_turn == DIRECTIONS['right']:
        if head_pos['eye_direct'] == DIRECTIONS['right']:
            head_pos['j'] += 1
    elif player_turn == DIRECTIONS['back']:
        if head_pos['eye_direct'] == DIRECTIONS['back']:
            head_pos['i'] += 1
    elif player_turn == DIRECTIONS['left']:
        if head_pos['eye_direct'] == DIRECTIONS['left']:
            head_pos['j'] -= 1

    return head_pos


def tank_move(playing_field: tuple, player_turn: str) -> tuple:
    """
        Принимает на вход текущее состояние игрового поля, а также ход игрока,
        после чего вносит в игровое поле изменения в соответствии со сделанным ходом,
        возвращая в итоге новое, измененное состояние игрового поля для отрисовки (вывода).
    """
    global current_head_pos
    field_len = len(playing_field[0])
    field_wid = len(playing_field)
    current_head_pos = head_move(player_turn, current_head_pos)
    playing_field = create_field(field_len,
                                 field_wid,
                                 current_head_pos)
    # else:
    #     print('WRONG TURN')

    return playing_field


def clear_window() -> None:
    """
        Очищает окно для начала отрисовки следующего кадра.
    """
    os.system('cls')
