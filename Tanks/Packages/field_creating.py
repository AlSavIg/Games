from .constants import START_HEAD_POS
from .calc_pos_of_objects import make_tank, head_move

current_head_pos = START_HEAD_POS.copy()


def create_field(player_turn='',
                 length=10,
                 width=10) -> tuple:
    """
        Функция принимает на вход значения длины и ширины игрового поля,
        а также текущий ход игрока,
        после чего возвращает кортеж, представляющий собой матрицу
        соответствующего размера с отрисованным в необходимой позиции танком.
        Элементы кортежа - списки (изменяемы).
        Если вызвать функцию без объявления аргументов, то
        то будет сгенерирована матрица стандартного размера (10 на 10 'пикселей').
        Модель 'танка' по умолчанию располагается в левом верхнем углу.
    """
    playing_field = [[0] * length for i in range(width)]

    global current_head_pos

    current_head_pos = head_move(player_turn,
                                 current_head_pos,
                                 length,
                                 width)

    tank_coord = make_tank(length,
                           width,
                           current_head_pos)

    for coord in tank_coord:
        playing_field[coord[0]][coord[1]] = 1
    playing_field = tuple(playing_field)

    return playing_field


# [print(*row, sep='') for row in create_field()]
# print(create_field())
# Debugging prints
