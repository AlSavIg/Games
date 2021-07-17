# import keyboard
# from rendering import render
# from field_creating import create_field
# Временная абсолютная ссылка для проверки работоспособности этого модуля отдельно от других

# from .rendering import render
# from .field_creating import create_field
# Относительные ссылки работают ТОЛЬКО при вызове модуля другим, главным, модулем
# __init__.py не обязателен (version Python 3.3 and more), создан только чтобы не раздражать PyCharm


def control_signal() -> str:
    """
        Ожидает нажатия игроком управляющих клавиш.
        После нажатия возвращает символ, введенный игроком.
    """
    signal = input('Движение осуществляется на клавиши W A S D:\n' +
                   'Ходите!\n')
    return signal
