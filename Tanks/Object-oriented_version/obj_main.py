import os
import time
from abc import ABCMeta
from termcolor import cprint
from threading import Thread
from pynput import keyboard


class MapFeatures(metaclass=ABCMeta):
    """
        Содержит все необходимые характеристики игрового поля.
        Также создает (public) атрибуты, которые содержат информацию
        о размерах игровой карты.
    """
    length = 10
    width = 10
    values_of_matrix_elem = {'map': 0,
                             'tank': 1,
                             'cannon_ball': 2}

    def __init__(self, length, width):
        self.length = length
        self.width = width
        MapFeatures.length = length
        MapFeatures.width = width


class Map(MapFeatures):
    def __init__(self,
                 length=MapFeatures.length,
                 width=MapFeatures.width):
        super().__init__(length, width)
        self.map = self.__clear_map()

    def __clear_map(self):
        return [[0] * self.length for _ in range(self.width)]

    def display_obj(self, *args):
        self.map = self.__clear_map()
        for mov_obj in args:
            if mov_obj.name == 'tank':
                mov_obj.make_body()
                for i, j in mov_obj.body:
                    self.map[i][j] = 1
            elif mov_obj.name == 'cannon_ball' and mov_obj.visibility:
                self.map[mov_obj.i][mov_obj.j] = 2


class MovingObjects:
    DIRECTIONS = {'up': 'w',
                  'down': 's',
                  'right': 'd',
                  'left': 'a'}
    START_HEAD_POS = {'i': 1,
                      'j': 3,
                      'direction': 'd'}

    def __init__(self,
                 i=START_HEAD_POS['i'],
                 j=START_HEAD_POS['j'],
                 direction=START_HEAD_POS['direction']):
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

    def return_attributes(self):
        return {'i': self.i,
                'j': self.j,
                'direction': self.direction}

    def simplest_move(self):
        directions = MovingObjects.DIRECTIONS
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
    def __init__(self):
        super().__init__()
        self.name = 'tank'
        self.body = set()

    def make_body(self):
        directions = MovingObjects.DIRECTIONS
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
        DIRECTIONS = super().DIRECTIONS
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
    list_with_balls = []

    def __init__(self, visibility=True):
        super().__init__()
        self.name = 'cannon_ball'
        self.visibility = visibility

    @classmethod
    def throw_garbage(cls):
        for ball in cls.list_with_balls:
            if not ball.visibility:
                cls.list_with_balls.remove(ball)

    def shoot(self, head):
        self.direction = cur_direct = head.direction
        directions = MovingObjects.DIRECTIONS
        i = j = int()

        if cur_direct == directions['up']:
            i, j = MovingObjects.move_up(head.i, head.j, 1)
        elif cur_direct == directions['right']:
            i, j = MovingObjects.move_right(head.i, head.j, 1)
        elif cur_direct == directions['down']:
            i, j = MovingObjects.move_down(head.i, head.j, 1)
        elif cur_direct == directions['left']:
            i, j = MovingObjects.move_left(head.i, head.j, 1)

        self.i, self.j = MovingObjects.deduction_ring(i, j)
        CannonBall.list_with_balls.append(self)

    def collision(self, map_obj):
        if 0 <= self.i < map_obj.width and \
                0 <= self.j < map_obj.length:
            if map_obj.map[self.i][self.j] != MapFeatures.values_of_matrix_elem['map'] and \
               map_obj.map[self.i][self.j] != MapFeatures.values_of_matrix_elem['cannon_ball']:
                self.visibility = False
        else:
            self.visibility = False

    def simplest_move(self):
        directions = MovingObjects.DIRECTIONS
        i = j = int()
        if self.direction == directions['right']:
            i, j = MovingObjects.move_right(self.i, self.j)
        elif self.direction == directions['left']:
            i, j = MovingObjects.move_left(self.i, self.j)
        elif self.direction == directions['up']:
            i, j = MovingObjects.move_up(self.i, self.j)
        elif self.direction == directions['down']:
            i, j = MovingObjects.move_down(self.i, self.j)

        self.i, self.j = i, j


def render(rendering_obj=None, menu=False) -> None:
    MENU = '\n\t\tТАНЧИК(И)\n' + \
           'Управление в игре осуществляется клавишами WASD,\n' + \
           'Для выхода из игры введите q\n' + \
           'Для того, чтобы начать, нажмите Enter\n'
    PIXEL_SIZE = 2

    def clear_console() -> None:
        """
            Очищает окно для начала отрисовки следующего кадра.
        """
        os.system('cls')

    if menu:
        rendering_obj = MENU

    clear_console()

    if isinstance(rendering_obj, list):
        def colorize(color_obj) -> None:
            nonlocal PIXEL_SIZE
            """
                Принимает в качестве аргумента объект,
                после чего выводит в консоль пиксель
                или строку
                определенного цвета, следуя следующей схеме:
                0 - 'поле' - белый
                1 - 'танк' - синий
                2 - 'снаряд' - красный
            """
            if isinstance(color_obj, list):
                cprint(' ' * PIXEL_SIZE * MapFeatures.length,
                       on_color='on_white',
                       sep='',
                       end='\n')
            elif isinstance(color_obj, int):
                if color_obj == MapFeatures.values_of_matrix_elem['map']:
                    cprint(' ' * PIXEL_SIZE,
                           on_color='on_white',
                           sep='',
                           end='')
                elif color_obj == MapFeatures.values_of_matrix_elem['tank']:
                    cprint(' ' * PIXEL_SIZE,
                           on_color='on_blue',
                           sep='',
                           end='')
                elif color_obj == MapFeatures.values_of_matrix_elem['cannon_ball']:
                    cprint(' ' * PIXEL_SIZE,
                           on_color='on_red',
                           sep='',
                           end='')

        """
            Принимает в качестве аргумента объект для отрисовки
            и выводит (отрисовывает) его в консоль в соответствии с цветом пикселя,
            который задается цифрой, являющейся элементом матрицы,
            где соблюдается следующее соответствие:
            0 - 'поле' - белый
            1 - 'танк' - синий
            2 - 'снаряд' - красный
        """
        for row in rendering_obj:
            if row.count(0) == MapFeatures.length:
                colorize(row)
                continue
            for column in row:
                colorize(column)
            print()
        print('\n')

    elif isinstance(rendering_obj, str):
        cprint(str.upper(rendering_obj), on_color='on_green', color='blue')


class MyThread(Thread):
    """A threading example"""

    def __init__(self, name):
        """Инициализация потока"""
        Thread.__init__(self)
        self.name = name

    my_turn = str()

    def run(self):
        """Запуск потока"""
        if self.name == 'output':
            game_map = Map()
            tank = Tank()

            render(menu=True)
            input()

            while MyThread.my_turn != 'q':
                balls_list = getattr(CannonBall, 'list_with_balls')
                if MyThread.my_turn != ' ':
                    tank.move_head(MyThread.my_turn)
                    for cannon_ball in balls_list:
                        cannon_ball.simplest_move()
                else:
                    CannonBall().shoot(tank)
                for cannon_ball in balls_list:
                    cannon_ball.collision(game_map)
                game_map.display_obj(tank, *balls_list)
                CannonBall.throw_garbage()
                render(game_map.map)
                MyThread.my_turn = str()
                time.sleep(0.5)
            else:
                render('game over')

        elif self.name == 'input':
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

            start_read()


def create_threads():
    """Создаем группу потоков"""
    input_thread = MyThread('input')
    output_thread = MyThread('output')
    input_thread.start()
    output_thread.start()


if __name__ == '__main__':
    create_threads()
