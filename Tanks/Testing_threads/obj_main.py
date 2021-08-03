import os
import time
from abc import ABCMeta
from termcolor import cprint

LENGTH = 10
WIDTH = 10


class MapFeatures(metaclass=ABCMeta):
    length = width = int()

    def __init__(self, length, width):
        self.length = length
        self.width = width
        MapFeatures.length = length
        MapFeatures.width = width


class Map(MapFeatures):
    def __init__(self, length=LENGTH, width=WIDTH):
        super().__init__(length, width)
        self.map = self.__clear_map()

    def __clear_map(self):
        return [[0] * self.length for _ in range(self.width)]

    def create_object(self, mov_obj):
        self.map = self.__clear_map()
        if mov_obj.name == 'tank':
            mov_obj.make_body()
            for i, j in mov_obj.body:
                self.map[i][j] = 1
        elif mov_obj.name == 'cannon_ball':
            self.map[mov_obj.i][mov_obj.j] = 2


class MovingObjects:
    _DIRECTIONS = {'up': 'w',
                   'down': 's',
                   'right': 'd',
                   'left': 'a'}

    def __init__(self, i, j, direction):
        self.i = i
        self.j = j
        self.direction = direction

    @staticmethod
    def deduction_ring(i, j):
        return i % MapFeatures.width, j % MapFeatures.length

    @staticmethod
    def move_up(i, j):
        return i - 1, j

    @staticmethod
    def move_down(i, j):
        return i + 1, j

    @staticmethod
    def move_left(i, j):
        return i, j - 1

    @staticmethod
    def move_right(i, j):
        return i, j + 1

    def simplest_move(self):
        directions = MovingObjects._DIRECTIONS
        i = j = int()
        if self.direction == directions['right']:
            i, j = MovingObjects.move_right(self.i, self.j)
        elif self.direction == directions['left']:
            i, j = MovingObjects.move_left(self.i, self.j)
        elif self.direction == directions['up']:
            i, j = MovingObjects.move_up(self.i, self.j)
        elif self.direction == directions['down']:
            i, j = MovingObjects.move_down(self.i, self.j)

        self.i, self.j = MovingObjects.deduction_ring(i, j)


class Tank(MovingObjects):
    def __init__(self, pos: dict):
        super().__init__(**pos)
        self.name = 'tank'
        # start pos of the tank in coordinates
        self.body = {(0, 0), (0, 1), (0, 2),
                     (1, 0), (1, 1), (1, 2), (1, 3),
                     (2, 0), (2, 1), (2, 2)}

    def make_body(self):
        directions = MovingObjects._DIRECTIONS
        i, j, direction = self.i, self.j, self.direction

        tank_coord = {(i, j)}

        if direction == directions['up']:
            for k in range(i + 1, i + 4):
                for z in range(j - 1, j + 2):
                    tank_coord.add(MovingObjects.deduction_ring(k, z))
        elif direction == directions['right']:
            for k in range(i - 1, i + 2):
                for z in range(j - 3, j):
                    tank_coord.add(MovingObjects.deduction_ring(k, z))
        elif direction == directions['back']:
            for k in range(i - 3, i):
                for z in range(j - 1, j + 2):
                    tank_coord.add(MovingObjects.deduction_ring(k, z))
        elif direction == directions['left']:
            for k in range(i - 1, i + 2):
                for z in range(j + 1, j + 4):
                    tank_coord.add(MovingObjects.deduction_ring(k, z))

        self.body = tank_coord


class CannonBall(MovingObjects):
    def __init__(self, pos: dict):
        super().__init__(**pos)
        self.name = 'cannon_ball'


def control_signal() -> str:
    """
        Ожидает нажатия игроком управляющих клавиш.
        После нажатия возвращает символ, введенный игроком.
    """
    signal = input('Движение осуществляется на клавиши W A S D:\n' +
                   'Ваш ход: ')
    return signal


def print_menu() -> None:
    """
        Выводит на экран меню, ожидая нажатия Enter.
    """
    print('\n\t\t\t\tТАНЧИК(И)\n' +
          'Управление в игре осуществляется клавишами WASD,\n' +
          # 'после ввода которых необходимо подтвердить ход нажатием Enter\n' +
          # 'Для выхода из игры введите quit и нажмите Enter\n' +
          'Для выхода из игры введите q\n' +
          'Для того, чтобы начать, нажмите Enter\n', end='')
    input()


def render(playing_field: tuple) -> None:

    pixel_size = 2

    def colorize(color: int) -> None:
        nonlocal pixel_size
        """
            Принимает в качестве аргумента число,
            после чего выводит в консоль пиксель
            определенного цвета, следуя следующей схеме:
            0 - 'поле' - белый
            1 - 'танк' - синий
            2 - 'снаряд' - красный
        """
        if color == 0:
            cprint(' ' * pixel_size, on_color='on_white', sep='', end='')
        elif color == 1:
            cprint(' ' * pixel_size, on_color='on_blue', sep='', end='')
        elif color == 2:
            cprint(' ' * pixel_size, on_color='on_red', sep='', end='')

    """
        Принимает в качестве аргумента кортеж - матрицу (игровое поле)
        и выводит (отрисовывает) его в консоль в соответствии с цветом пикселя,
        который задается цифрой, являющейся элементом матрицы,
        где соблюдается следующее соответствие:
        0 - 'поле' - белый
        1 - 'танк' - синий
        2 - 'снаряд' - красный
    """
    for row in playing_field:
        for column in row:
            colorize(column)
        print()
    print('\n')


def clear_console() -> None:
    """
        Очищает окно для начала отрисовки следующего кадра.
    """
    os.system('cls')


START_HEAD_POS = {'i': 1,
                  'j': 3,
                  'direction': 'd'}


def main():

    # turn = str()

    def meeting_messages(map_):
        # nonlocal turn
        print_menu()
        clear_console()
        render(map_.map)
        # turn = control_signal()

    def make_turn(map_, tank_):
        # nonlocal turn
        clear_console()
        tank_.simplest_move()
        map_.create_object(tank_)
        render(map_.map)
        time.sleep(1)
        # turn = control_signal()

    game_map = Map()
    tank = Tank(START_HEAD_POS)

    meeting_messages(game_map)
    for _ in range(10):
        make_turn(game_map, tank)

    # cannon_ball = CannonBall()


if __name__ == '__main__':
    main()
