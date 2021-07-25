from .constants import LENGTH, WIDTH


def move_right(head_pos: dict, num_moves: int) -> dict:
    """
        Принимает на вход позицию 'дула' ('head') танка
        в формате (i, j, eye_direct),
        а также количество 'клеток', на которые необходимо совершить перемещение
        в выбранном направлении
        (направо, считая, что начало координат находится в левом верхнем углу).
        Возвращает новую позицию 'дула' ('head') танка.
    """
    head_pos['j'] += num_moves
    head_pos['j'] %= LENGTH

    return head_pos


def move_left(head_pos: dict, num_moves: int) -> dict:
    """
        Принимает на вход позицию 'дула' ('head') танка
        в формате (i, j, eye_direct),
        а также количество 'клеток', на которые необходимо совершить перемещение
        в выбранном направлении
        (налево, считая, что начало координат находится в левом верхнем углу).
        Возвращает новую позицию 'дула' ('head') танка.
    """
    head_pos['j'] -= num_moves
    head_pos['j'] %= LENGTH

    return head_pos


def move_straight(head_pos: dict, num_moves: int) -> dict:
    """
        Принимает на вход позицию 'дула' ('head') танка
        в формате (i, j, eye_direct),
        а также количество 'клеток', на которые необходимо совершить перемещение
        в выбранном направлении
        (вверх, считая, что начало координат находится в левом верхнем углу).
        Возвращает новую позицию 'дула' ('head') танка.
    """
    head_pos['i'] -= num_moves
    head_pos['i'] %= WIDTH

    return head_pos


def move_back(head_pos: dict, num_moves: int) -> dict:
    """
        Принимает на вход позицию 'дула' ('head') танка
        в формате (i, j, eye_direct),
        а также количество 'клеток', на которые необходимо совершить перемещение
        в выбранном направлении
        (вниз, считая, что начало координат находится в левом верхнем углу).
        Возвращает новую позицию 'дула' ('head') танка.
    """
    head_pos['i'] += num_moves
    head_pos['i'] %= WIDTH

    return head_pos


def move_back_and_right(head_pos: dict,
                        num_moves_back: int,
                        num_moves_right: int) -> dict:
    """
        Принимает на вход позицию 'дула' ('head') танка
        в формате (i, j, eye_direct),
        а также количество 'клеток', на которые необходимо совершить перемещение
        в выбранном направлении в каждую сторону
        в формате: количество ходов вниз, количество ходов вправо
        (считая, что начало координат находится в левом верхнем углу).
        Возвращает новую позицию 'дула' ('head') танка.
    """
    head_pos = move_back(head_pos, num_moves_back)
    head_pos = move_right(head_pos, num_moves_right)

    return head_pos


def move_back_and_left(head_pos: dict,
                       num_moves_back: int,
                       num_moves_left: int) -> dict:
    """
        Принимает на вход позицию 'дула' ('head') танка
        в формате (i, j, eye_direct),
        а также количество 'клеток', на которые необходимо совершить перемещение
        в выбранном направлении в каждую сторону
        в формате: количество ходов вниз, количество ходов влево
        (считая, что начало координат находится в левом верхнем углу).
        Возвращает новую позицию 'дула' ('head') танка.
    """
    head_pos = move_back(head_pos, num_moves_back)
    head_pos = move_left(head_pos, num_moves_left)

    return head_pos


def move_straight_and_left(head_pos: dict,
                           num_moves_straight: int,
                           num_moves_left: int) -> dict:
    """
        Принимает на вход позицию 'дула' ('head') танка
        в формате (i, j, eye_direct),
        а также количество 'клеток', на которые необходимо совершить перемещение
        в выбранном направлении в каждую сторону
        в формате: количество ходов вверх, количество ходов влево
        (считая, что начало координат находится в левом верхнем углу).
        Возвращает новую позицию 'дула' ('head') танка.
    """
    head_pos = move_straight(head_pos, num_moves_straight)
    head_pos = move_left(head_pos, num_moves_left)

    return head_pos


def move_straight_and_right(head_pos: dict,
                            num_moves_straight: int,
                            num_moves_right: int) -> dict:
    """
        Принимает на вход позицию 'дула' ('head') танка
        в формате (i, j, eye_direct),
        а также количество 'клеток', на которые необходимо совершить перемещение
        в выбранном направлении в каждую сторону
        в формате: количество ходов вверх, количество ходов вправо
        (считая, что начало координат находится в левом верхнем углу).
        Возвращает новую позицию 'дула' ('head') танка.
    """
    head_pos = move_straight(head_pos, num_moves_straight)
    head_pos = move_right(head_pos, num_moves_right)

    return head_pos
