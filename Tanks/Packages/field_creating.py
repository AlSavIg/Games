def create_field(length=10, width=10, head_pos=(1, 3)) -> tuple:
    """
    Функция принимает на вход значения длины и ширины игрового поля,
    а также позицию 'дула' танка ('head'),
    после чего возвращает кортеж, представляющий собой матрицу
    соответствующего размера с отрисованным в необходимой позиции танком.
    Элементы кортежа - списки (изменяемы).
    Если вызвать функцию без объявления аргументов, то
    то будет сгенерирована матрица стандартного размера: 10 на 10 'пикселей'.
    Модель 'танка' по умолчанию располагается в левом верхнем углу.
    """
    playing_field = [[0] * length for i in range(width)]
    # tank_pattern = ((1, 1, 1),
    #                 (1, 1, 1, 1),
    #                 (1, 1, 1))
    # tank_pattern_coordinates = {(0, 0), (0, 1), (0, 2),
    #                             (1, 0), (1, 1), (1, 2), (1, 3),
    #                             (2, 0), (2, 1), (2, 2)}
    i = head_pos[0]
    j = head_pos[1]
    tank_pattern_coordinates = {(i - 1, j - 3), (i - 1, j - 2), (i - 1, j - 1),
                                (i, j - 3), (i, j - 2), (i, j - 1), (i, j),
                                (i + 1, j - 3), (i + 1, j - 2), (i + 1, j - 1)}
    for coord in tank_pattern_coordinates:
        playing_field[coord[0]][coord[1]] = 1
    playing_field = tuple(playing_field)

    return playing_field


# [print(*row, sep='') for row in create_field()]
# print(create_field())
# Debugging prints
