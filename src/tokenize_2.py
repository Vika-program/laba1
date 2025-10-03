from src.other import is_num, is_op, CalcError, is_un, re


def tokenize_2(expr):
    """
    Разбивает математическое выражение на токены, параллельно проверяя, что оно корректно
    :param expr: исходное математическое выражение
    :return: список токенов
    """
    new_expr = ''
    open_brackets = 0
    if is_op(expr.rstrip()[-1]): # строка заканчивается на операцию
        raise CalcError('Не хватает числа')
    if re.findall(r"\d+\s+\d+", expr): #два числа идут подряд через пробел
        raise CalcError('Два числа не могут стоять рядом')
    for tok in expr:
        if tok == ' ':
            continue
        elif tok == '.' and new_expr and is_num(new_expr[-1]):
            new_expr += tok
        elif is_op(tok) and is_un(tok, new_expr):
            new_expr += ' ' + f'u{tok}'          # добавляем u к унарному оператору
        elif (tok in '*/&#%+-' and new_expr and
              new_expr[-1] not in '+-*/&#%('): # условия для остальных операций
            new_expr += ' ' + tok
        elif (is_num(tok) and new_expr and (is_num(new_expr[-1])
                                            or new_expr[-1] == '.')): #если последней была цифра, то не будет пробела
            new_expr += tok
        elif is_num(tok) and (not new_expr or not is_num(new_expr[-1])): #если начинается новое чило, ставим пробел
            new_expr += ' ' + tok
        elif (tok == '(' and (not new_expr or (not is_num(new_expr[-1])
                                               and new_expr[-1] != ')'))): # ( идёт в начале строке или не после числа и )
            new_expr += ' ' + tok
            open_brackets += 1
        elif (tok == ')' and new_expr and not is_op(new_expr[-1])
              and new_expr[-1] != '('):            #перед скобкой ) не может быть числа и (
            new_expr += ' ' + tok
            open_brackets -= 1
        elif not is_num(tok) and not is_op(tok) and tok not in '.()':
            raise CalcError("Недопустимый символ")
        else:
            raise CalcError("Ошибка синтаксиса")
        if open_brackets < 0:
            raise CalcError("Не хватает открывающей скобки")
    if open_brackets > 0:
        raise CalcError("Не хватает закрывающей скобки")
    return new_expr.split()
