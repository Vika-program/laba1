from src.other import is_op, is_num, CalcError
from src.tokenize import tokenize
from src.is_correct import is_correct

PRIO = {'+': 1, '-': 1, '*': 2, '/': 2, '&': 2, '%': 2, '#': 3, 'u+': 4, 'u-': 4} #словарь с приоритетами операций


def trans_to_rpn(expr):
    """
    Переводит математическое выражение в обратную польскую запись
    :param expr: атематическое выражение в инфиксной записи
    :return: возвращает выражение в обратнуй польской записи
    """
    res = []
    op_trans = [] #список с операциями и скобками
    if not expr:
        raise CalcError('Пустой ввод')
    expr = expr.replace('//', '&').replace('**', '#') #заменяем // на &, ** на #
    expr = tokenize(expr)
    is_correct(expr)
    for tok in expr:
        if is_num(tok):
            res.append(tok)
        elif is_op(tok):
            if tok != "#":
                while (op_trans and is_op(op_trans[-1]) and
                       PRIO[op_trans[-1]] >= PRIO[tok]):
                    res.append(op_trans.pop())
            else:
#проверяем, что op_trans не пустой список, последний символ является операцией и выше по приоритету, чем последний в op_trans
                while (op_trans and is_op(op_trans[-1]) and
                       PRIO[op_trans[-1]] > PRIO[tok]):
                    res.append(op_trans.pop())
            op_trans.append(tok)
        elif tok == '(':
            op_trans.append(tok)
        elif tok == ')':
            while op_trans and op_trans[-1] != '(':
                res.append(op_trans.pop())
            if op_trans and op_trans[-1] == '(':
                op_trans.pop()
    while op_trans:
        res.append(op_trans.pop())
    return res
