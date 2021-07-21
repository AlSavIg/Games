from .constants import DIRECTIONS
from .trivial_move import move_straight_and_left, \
                          move_straight_and_right, \
                          move_back_and_right, \
                          move_back_and_left


def head_move(player_turn: str,
              head_pos: dict) -> dict:
    """
        Принимает на вход ход игрока и текущее положение 'дула' ('head') танка.
        Возвращает новое положение 'дула' ('head') танка.
    """
    if player_turn == DIRECTIONS['straight']:
        if head_pos['eye_direct'] == DIRECTIONS['straight']:
            head_pos = move_straight_and_right(head_pos, 1, 0)
        elif head_pos['eye_direct'] == DIRECTIONS['right']:
            head_pos = move_straight_and_left(head_pos, 2, 2)
        elif head_pos['eye_direct'] == DIRECTIONS['back']:
            head_pos = move_straight_and_right(head_pos, 4, 0)
        elif head_pos['eye_direct'] == DIRECTIONS['left']:
            head_pos = move_straight_and_right(head_pos, 2, 2)
        head_pos['eye_direct'] = DIRECTIONS['straight']
    elif player_turn == DIRECTIONS['right']:
        if head_pos['eye_direct'] == DIRECTIONS['right']:
            head_pos = move_back_and_right(head_pos, 0, 1)
        elif head_pos['eye_direct'] == DIRECTIONS['straight']:
            head_pos = move_back_and_right(head_pos, 2, 2)
        elif head_pos['eye_direct'] == DIRECTIONS['left']:
            head_pos = move_back_and_right(head_pos, 0, 4)
        elif head_pos['eye_direct'] == DIRECTIONS['back']:
            head_pos = move_straight_and_right(head_pos, 2, 2)
        head_pos['eye_direct'] = DIRECTIONS['right']
    elif player_turn == DIRECTIONS['back']:
        if head_pos['eye_direct'] == DIRECTIONS['back']:
            head_pos = move_back_and_left(head_pos, 1, 0)
        elif head_pos['eye_direct'] == DIRECTIONS['right']:
            head_pos = move_back_and_left(head_pos, 2, 2)
        elif head_pos['eye_direct'] == DIRECTIONS['straight']:
            head_pos = move_back_and_right(head_pos, 4, 0)
        elif head_pos['eye_direct'] == DIRECTIONS['left']:
            head_pos = move_back_and_right(head_pos, 2, 2)
        head_pos['eye_direct'] = DIRECTIONS['back']
    elif player_turn == DIRECTIONS['left']:
        if head_pos['eye_direct'] == DIRECTIONS['left']:
            head_pos = move_back_and_left(head_pos, 0, 1)
        elif head_pos['eye_direct'] == DIRECTIONS['straight']:
            head_pos = move_back_and_left(head_pos, 2, 2)
        elif head_pos['eye_direct'] == DIRECTIONS['right']:
            head_pos = move_back_and_left(head_pos, 0, 4)
        elif head_pos['eye_direct'] == DIRECTIONS['back']:
            head_pos = move_straight_and_left(head_pos, 2, 2)
        head_pos['eye_direct'] = DIRECTIONS['left']

    return head_pos


def make_tank(length: int,
              width: int,
              head_pos: dict) -> set:
    """
        Принимает в качестве аргументов длину, ширину поля,
        а также текущее положение 'дула' ('head') танка.
        Возвращает множество, содержащее координаты,
        в форме кортежей из 2-х значений (i и j или х и у),
        в которых назодится танк в текущий момент,
        используя кольца вычетов по модулю length или width.
        *** При переходе через границы игрового поля
            танк появится с противоположной стороны.
    """
    i, j, eye_direct = head_pos['i'], head_pos['j'], head_pos['eye_direct']
    tank_coordinates = {(i % width, j % length)}

    if eye_direct == DIRECTIONS['straight']:
        for k in range(i + 1, i + 4):
            for z in range(j - 1, j + 2):
                tank_coordinates.add((k % width, z % length))
    elif eye_direct == DIRECTIONS['right']:
        for k in range(i - 1, i + 2):
            for z in range(j - 3, j):
                tank_coordinates.add((k % width, z % length))
    elif eye_direct == DIRECTIONS['back']:
        for k in range(i - 3, i):
            for z in range(j - 1, j + 2):
                tank_coordinates.add((k % width, z % length))
    elif eye_direct == DIRECTIONS['left']:
        for k in range(i - 1, i + 2):
            for z in range(j + 1, j + 4):
                tank_coordinates.add((k % width, z % length))

    return tank_coordinates
