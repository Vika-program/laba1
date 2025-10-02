import string


def tokenize(expr):
    """Разбивает выражение на токены
    :param: expr: принимает математическое выражение (с уже произведённой заменой ** на # и // на &)
    :return: возвращает выражение, разбитое на токены"""
    new_expr = ''
    for x in expr:
        if x in string.digits or (x == '.' and new_expr[-1] in string.digits): #не ставим пробел между цифрами и частью дробного числа
            new_expr += x
        elif x == ' ':
            continue
        elif x in '+-' and len(new_expr) >= 2 and new_expr[-2] == '(': # обрабатываем унарные знаки
            new_expr += x
        else:
            new_expr += (' ' + x + ' ')
    return new_expr.split()
