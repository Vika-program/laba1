import re


def is_num(num):
    """проверяет, что токен является целым числом или десятичной дробью
    :param num: токен
    :return: истина или ложь"""
    if re.fullmatch(r'[-+]?\d+(?:.\d+)?', num):
        return True
    return False


def is_op(op):
    """проверяет, что токен является операцией
    :param num: токен
    :return: истина или ложь"""
    return op in ['#', '+', '-', '&', '*', '%', '/']



class CalcError(Exception):
    # класс ошибок
    pass