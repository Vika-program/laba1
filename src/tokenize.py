import string
from src.other import is_un, is_op


def tokenize(expr):
    """
    Разбивает выражение на токены
    :param expr: принимает математическое выражение в инфиксной записи
    :return: возвращает вписок токенов
    """
    new_expr = []
    current_num = ''
    for tok in expr:
        if tok in string.digits:
            current_num += tok
        elif tok == '.' and current_num:
            current_num += tok
        else:
            # добавляем текущее число в new_expr и сбрасываем current
            if current_num:
                new_expr.append(current_num)
            current_num = ''
            if tok == ' ':
                pass
            # для унарных операторов
            elif is_op(tok) and is_un(tok, new_expr):
                new_expr.append(f'u{tok}')
            else:
                new_expr.append(tok)
    new_expr.append(current_num)
    return new_expr
