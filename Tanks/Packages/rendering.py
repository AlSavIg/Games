from termcolor import cprint


PIXEL_SIZE = 2


def colorize(color: int) -> None:
    """
        Принимает в качестве аргумента число,
        после чего выводит в консоль пиксель
        определенного цвета, следуя следующей схеме:
        0 - 'поле' - белый
        1 - 'танк' - синий
        2 - 'снаряд' - красный
        *** Используются функции пакета termcolor
    """
    if color == 0:
        cprint(' ' * PIXEL_SIZE, on_color='on_white', sep='', end='')
    elif color == 1:
        cprint(' ' * PIXEL_SIZE, on_color='on_blue', sep='', end='')
    elif color == 2:
        cprint(' ' * PIXEL_SIZE, on_color='on_red', sep='', end='')


def render(playing_field: tuple) -> None:
    """
        Принимает в качестве аргумента кортеж - матрицу (игровое поле)
        и выводит (отрисовывает) его в консоль в соответствии с цветом пикселя,
        который задается цифрой, являющейся элементом матрицы,
        где соблюдается следующее соответствие:
        0 - 'поле' - белый
        1 - 'танк' - синий
        2 - 'снаряд' - красный
        *** Используются функции пакета termcolor
    """
    for row in playing_field:
        for column in row:
            colorize(column)
        print()

