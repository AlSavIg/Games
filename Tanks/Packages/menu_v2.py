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
