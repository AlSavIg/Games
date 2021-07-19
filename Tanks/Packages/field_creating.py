from .constants import START_HEAD_POS
from .calc_pos_of_objects import make_tank, head_move


current_head_pos = START_HEAD_POS.copy()


def create_field(length=10,
                 width=10,
                 head_pos=START_HEAD_POS.copy()) -> tuple:
    """
        Функция принимает на вход значения длины и ширины игрового поля,
        а также позицию 'дула' танка ('head'),
        после чего возвращает кортеж, представляющий собой матрицу
        соответствующего размера с отрисованным в необходимой позиции танком.
        Элементы кортежа - списки (изменяемы).
        Если вызвать функцию без объявления аргументов, то
        то будет сгенерирована матрица стандартного размера (10 на 10 'пикселей').
        Модель 'танка' по умолчанию располагается в левом верхнем углу.
    """
    playing_field = [[0] * length for i in range(width)]
    tank_coord = make_tank(length, width, head_pos)
    for coord in tank_coord:
        playing_field[coord[0]][coord[1]] = 1
    playing_field = tuple(playing_field)

    return playing_field


def tank_pos(playing_field: tuple, player_turn: str) -> tuple:
    """
        Принимает на вход текущее состояние игрового поля, а также ход игрока,
        после чего вносит в игровое поле изменения в соответствии со сделанным ходом,
        возвращая в итоге новое, измененное состояние игрового поля для отрисовки (вывода).
    """
    global current_head_pos
    field_len = len(playing_field[0])
    field_wid = len(playing_field)
    current_head_pos = head_move(player_turn,
                                 current_head_pos,
                                 field_len,
                                 field_wid)
    playing_field = create_field(field_len,
                                 field_wid,
                                 current_head_pos)

    return playing_field


# [print(*row, sep='') for row in create_field()]
# print(create_field())
# Debugging prints
