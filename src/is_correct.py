from src.other import CalcError, is_num, is_op


def is_correct(expr):
    """
    Проверяет корректность выражения
    :param expr: список токенов
    :return: ничего не возвращает, вызывает ошибку, если что-то не так
    """
    open_brackets = 0
    for i in range(len(expr)):
        if i >= 1 and is_num(expr[i]) and is_num(expr[i - 1]):
            raise CalcError('Два числа не могут стоять рядом')
        elif not is_num(expr[i]) and not is_op(expr[i]) and expr[i] not in '()':
            raise CalcError('Недопустимый символ или неверно стоит точка')
        # проверка скобок
        elif expr[i] == '(':
            open_brackets += 1
        elif expr[i] == ')':
            open_brackets -= 1
        if open_brackets < 0:
            raise CalcError("Не хватает открывающей скобки")
    if open_brackets > 0:
        raise CalcError("Не хватает закрывающей скобки")
