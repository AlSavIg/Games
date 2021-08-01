import os


def clear_console() -> None:
    """
        Очищает окно для начала отрисовки следующего кадра.
    """
    # os.system('cls')  # Win
    os.system('clear')  # Linux
