from .constants import DIRECTIONS, LENGTH, WIDTH
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


def make_tank(head_pos: dict) -> set:
    """
        Принимает в качестве аргумента текущее положение 'дула' ('head') танка.
        Возвращает множество, содержащее координаты,
        в форме кортежей из 2-х значений (i и j или х и у),
        в которых назодится танк в текущий момент,
        используя кольца вычетов по модулю length или width (globals).
        *** При переходе через границы игрового поля
            танк появится с противоположной стороны.
    """
    i, j, eye_direct = head_pos['i'], head_pos['j'], head_pos['eye_direct']
    tank_coordinates = {(i % LENGTH, j % WIDTH)}

    if eye_direct == DIRECTIONS['straight']:
        for k in range(i + 1, i + 4):
            for z in range(j - 1, j + 2):
                tank_coordinates.add((k % LENGTH, z % WIDTH))
    elif eye_direct == DIRECTIONS['right']:
        for k in range(i - 1, i + 2):
            for z in range(j - 3, j):
                tank_coordinates.add((k % LENGTH, z % WIDTH))
    elif eye_direct == DIRECTIONS['back']:
        for k in range(i - 3, i):
            for z in range(j - 1, j + 2):
                tank_coordinates.add((k % LENGTH, z % WIDTH))
    elif eye_direct == DIRECTIONS['left']:
        for k in range(i - 1, i + 2):
            for z in range(j + 1, j + 4):
                tank_coordinates.add((k % LENGTH, z % WIDTH))

    return tank_coordinates


def make_shoot(head_pos: dict) -> dict:
    """
        Принимает на вход позицию 'дула' ('head') танка в форме словаря
        формата (х (i), у(j), направление дула),
        а возвращает позицию ядра сразу после выстрела
        в формате (х (i), у(j), направление полета
                   (= направлению дула в момент выстрела))
    """
    eye_direct = head_pos['eye_direct']

    if eye_direct == DIRECTIONS['straight']:
        ball_pos = move_straight_and_left(head_pos, 1, 0)
    elif eye_direct == DIRECTIONS['right']:
        ball_pos = move_back_and_right(head_pos, 0, 1)
    elif eye_direct == DIRECTIONS['back']:
        ball_pos = move_back_and_left(head_pos, 1, 0)
    elif eye_direct == DIRECTIONS['left']:
        ball_pos = move_back_and_left(head_pos, 0, 1)

    return ball_pos
