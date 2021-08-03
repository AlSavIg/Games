import os
import time
from abc import ABCMeta
from termcolor import cprint
from threading import Thread
from pynput import keyboard

LENGTH = 10
WIDTH = 10


class MapFeatures(metaclass=ABCMeta):
    """
        Содержит все необходимые характеристики игрового поля.
        Также создает (public) атрибуты, которые содержат информацию
        о размерах игровой карты.
    """
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

    def display_obj(self, mov_obj):
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
    def move_up(i, j, num=1):
        return i - num, j

    @staticmethod
    def move_down(i, j, num=1):
        return i + num, j

    @staticmethod
    def move_left(i, j, num=1):
        return i, j - num

    @staticmethod
    def move_right(i, j, num=1):
        return i, j + num

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
        self.body = set()

    def make_body(self):
        directions = MovingObjects._DIRECTIONS
        i, j, direction = self.i, self.j, self.direction

        tank_coord = {MovingObjects.deduction_ring(i, j)}

        if direction == directions['up']:
            for k in range(i + 1, i + 4):
                for z in range(j - 1, j + 2):
                    tank_coord.add(MovingObjects.deduction_ring(k, z))
        elif direction == directions['right']:
            for k in range(i - 1, i + 2):
                for z in range(j - 3, j):
                    tank_coord.add(MovingObjects.deduction_ring(k, z))
        elif direction == directions['down']:
            for k in range(i - 3, i):
                for z in range(j - 1, j + 2):
                    tank_coord.add(MovingObjects.deduction_ring(k, z))
        elif direction == directions['left']:
            for k in range(i - 1, i + 2):
                for z in range(j + 1, j + 4):
                    tank_coord.add(MovingObjects.deduction_ring(k, z))

        self.body = tank_coord

    def move_head(self, player_turn: str):
        """
            Принимает на вход ход игрока.
            Изменяет атрибуты положения 'дула' ('head') танка.
        """
        DIRECTIONS = super()._DIRECTIONS
        if player_turn == DIRECTIONS['up']:
            if self.direction == DIRECTIONS['up']:
                self.i, self.j = MovingObjects.move_up(self.i, self.j, 1)
            elif self.direction == DIRECTIONS['right']:
                self.i, self.j = MovingObjects.move_left(*MovingObjects.move_up(self.i,
                                                                                self.j,
                                                                                2), 2)
            elif self.direction == DIRECTIONS['down']:
                self.i, self.j = MovingObjects.move_up(self.i, self.j, 4)
            elif self.direction == DIRECTIONS['left']:
                self.i, self.j = MovingObjects.move_right(*MovingObjects.move_up(self.i,
                                                                                 self.j,
                                                                                 2), 2)
            self.direction = DIRECTIONS['up']
        elif player_turn == DIRECTIONS['right']:
            if self.direction == DIRECTIONS['right']:
                self.i, self.j = MovingObjects.move_right(self.i, self.j, 1)
            elif self.direction == DIRECTIONS['up']:
                self.i, self.j = MovingObjects.move_right(*MovingObjects.move_down(self.i,
                                                                                   self.j,
                                                                                   2), 2)
            elif self.direction == DIRECTIONS['left']:
                self.i, self.j = MovingObjects.move_right(self.i, self.j, 4)
            elif self.direction == DIRECTIONS['down']:
                self.i, self.j = MovingObjects.move_right(*MovingObjects.move_up(self.i,
                                                                                 self.j,
                                                                                 2), 2)
            self.direction = DIRECTIONS['right']
        elif player_turn == DIRECTIONS['down']:
            if self.direction == DIRECTIONS['down']:
                self.i, self.j = MovingObjects.move_down(self.i, self.j, 1)
            elif self.direction == DIRECTIONS['right']:
                self.i, self.j = MovingObjects.move_left(*MovingObjects.move_down(self.i,
                                                                                  self.j,
                                                                                  2), 2)
            elif self.direction == DIRECTIONS['up']:
                self.i, self.j = MovingObjects.move_down(self.i, self.j, 4)
            elif self.direction == DIRECTIONS['left']:
                self.i, self.j = MovingObjects.move_right(*MovingObjects.move_down(self.i,
                                                                                   self.j,
                                                                                   2), 2)
            self.direction = DIRECTIONS['down']
        elif player_turn == DIRECTIONS['left']:
            if self.direction == DIRECTIONS['left']:
                self.i, self.j = MovingObjects.move_left(self.i, self.j, 1)
            elif self.direction == DIRECTIONS['up']:
                self.i, self.j = MovingObjects.move_left(*MovingObjects.move_down(self.i,
                                                                                  self.j,
                                                                                  2), 2)
            elif self.direction == DIRECTIONS['right']:
                self.i, self.j = MovingObjects.move_left(self.i, self.j, 4)
            elif self.direction == DIRECTIONS['down']:
                self.i, self.j = MovingObjects.move_left(*MovingObjects.move_up(self.i,
                                                                                self.j,
                                                                                2), 2)
            self.direction = DIRECTIONS['left']


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


class MyThread(Thread):
    """A threading example"""
    def __init__(self, name):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name

    my_turn = str()

    def run(self):
        """Запуск потока"""
        def make_turn(map_, tank_, flag=True):
            if not flag:
                print_menu()
            clear_console()
            tank_.move_head(MyThread.my_turn)
            map_.display_obj(tank_)
            render(map_.map)
            time.sleep(0.5)
            # turn = control_signal()

        def on_press(key: str) -> bool:
            """
                Внутри этой функции прописан код,
                который срабатывает всякий раз при нажатии определенной клавиши.
            """
            if key == keyboard.KeyCode(char='q'):
                MyThread.my_turn = 'q'
                return False
            elif key == keyboard.KeyCode(char='w'):
                MyThread.my_turn = 'w'
            elif key == keyboard.KeyCode(char='a'):
                MyThread.my_turn = 'a'
            elif key == keyboard.KeyCode(char='s'):
                MyThread.my_turn = 's'
            elif key == keyboard.KeyCode(char='d'):
                MyThread.my_turn = 'd'
            elif key == keyboard.Key.space:
                MyThread.my_turn = ' '

        def start_read() -> None:
            """Запускает процесс считывания с клавиатуры действий игрока в реальном времени."""
            with keyboard.Listener(on_press=on_press) as listener:
                listener.join()

        if self.name == 'output':
            game_map = Map()
            tank = Tank(START_HEAD_POS)

            make_turn(game_map, tank, False)
            while MyThread.my_turn != 'q':
                make_turn(game_map, tank)
            else:
                clear_console()
                print('GAME OVER')

        elif self.name == 'input':
            start_read()


def create_threads():
    """
    Создаем группу потоков
    """
    input_thread = MyThread('input')
    output_thread = MyThread('output')
    input_thread.start()
    output_thread.start()


if __name__ == '__main__':
    create_threads()
