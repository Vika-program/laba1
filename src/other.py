import re


def is_num(num):
    """
    проверяет, что токен является целым числом или десятичной дробью
    :param num: токен
    :return: истина или ложь
    """
    if re.fullmatch(r'[-+]?\d+(?:\.\d+)?', num):
        return True
    return False


def is_op(op):
    """
    проверяет, что токен является операцией
    :param op: токен
    :return: истина или ложь
    """
    return op in ['#', '+', '-', '&', '*', '%', '/', 'u-', 'u+']


def is_un(op, new_expr):
    """
    проверяет, является ли оператор унарным (используется в функции tokenize_2)
    :param op: оператор
    :param new_expr: выражение, которое существует на данный момент
    :return: Возвращает истину или ложь
    """
    if not new_expr or new_expr[-1] == '(':
        if op in '-+':
            return True
        else:
            raise CalcError('Неверный унарный оператор')
    return False


class CalcError(Exception):
    # класс ошибок
    pass
