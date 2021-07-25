from pynput import keyboard
from ..Packages.clear_console import clear_console
from ..Packages.field_creating import create_field
from ..Packages.constants import LENGTH, WIDTH
from ..Packages.rendering import render


def field_demo() -> None:
    """
        Производит вывод 'ознакомительной версии' игрового поля для игрока
        после нажатия на enter в меню.
    """
    clear_console()
    render(create_field(length=LENGTH, width=WIDTH))


def make_move(move: str) -> None:
    """
        Принимает на вход текущий ход игрока,
        а затем последовательно осуществляет:
        - Очистку консоли;
        - Генерацию игрового поля;
        - Отрисовку в консоль игрового поля;
    """
    player_turn = move
    clear_console()
    game_field = create_field(player_turn, LENGTH, WIDTH)
    render(game_field)


def on_press(key: str) -> bool:
    """
        Внутри этой функции прописан код,
        который срабатывает всякий раз при нажатии определенной клавиши.
    """
    # try:
    # print('alphanumeric key {0} pressed'.format(key))
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))
    # if key == keyboard.Key.esc:
    if key == keyboard.KeyCode(char='q'):
        clear_console()
        print('GAME_OVER')
        return False
    elif key == keyboard.KeyCode(char='w'):
        make_move('w')
    elif key == keyboard.KeyCode(char='a'):
        make_move('a')
    elif key == keyboard.KeyCode(char='s'):
        make_move('s')
    elif key == keyboard.KeyCode(char='d'):
        make_move('d')
    elif key == keyboard.Key.space:
        make_move(' ')


# def on_release(key):
#     print('{0} released'.format(
#         key))
#     if key == keyboard.Key.esc:
#         # Stop listener
#         return False


# Collect events until released
def start_read() -> None:
    """
        Запускает процесс считывания с клавиатуры действий игрока в реальном времени.
        *** Используется пакет pynput(.keyboard)
    """
    field_demo()
    with keyboard.Listener(on_press=on_press) as listener:  # , on_release=on_release) as listener:
        listener.join()


# # ...or, in a non-blocking fashion:
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()
