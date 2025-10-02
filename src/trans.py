from src.other import is_op, is_num, CalcError
from src.is_correct import is_correct
from src.tokenize import tokenize
from src.tokenize_2 import tokenize_2

prio = {'+': 1, '-': 1, '*': 2, '/': 2, '&': 2, '%': 2, '#': 3} #словарь с приоритетами операций


def trans_to_rpn(expr):
    """Переводит математическое выражение в обратную польскую запись
    :param expr: атематическое выражение в обычной записи
    :return: возвращает выражение в обратнуй польской записи"""
    res = []
    op_trans = [] #список с операциями и скобками
    if not expr:
        raise CalcError('Пустой ввод')
    expr = expr.replace('//', '&').replace('**', '#') #заменяем // на &, ** на #
    if not is_correct(expr):
        raise CalcError('Выражение некорректно') #раскомментировать стороку, если используете tokenize
    expr = tokenize(expr) # можно поменять на tokenize
    for tok in expr:
        if is_num(tok):
            res.append(tok)
        elif is_op(tok):
            # проверяем, что op_trans не пустой список, последний символ является операцией и выше или равен по приоритету последнему в op_trans
            while op_trans and is_op(op_trans[-1]) and prio[op_trans[-1]] >= prio[tok]:
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
