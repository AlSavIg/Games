def show_menu() -> str:
    """
        Выводит приветственное меню на экран и ожидает нажатия Enter,
        возвращая введенную пустую строку в качестве первого хода игрока.
    """
    print('ТАНЧИК(И)\n' +
          'Управление в игре осуществляется клавишами WASD,\n' +
          'после ввода которых необходимо подтвердить ход нажатием Enter\n' +
          'Для того, чтобы начать, нажмите Enter')
    player_turn = input()

    return player_turn
