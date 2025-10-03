from src.other import CalcError, is_num, is_op
from src.trans import trans_to_rpn

def calc(expr):
    """
    Вычисляет значение выражения
    :param expr: принимает выражение в обычной записи
    :return: возвращает результат вычисления
    """
    expr = trans_to_rpn(expr)
    stack = []
    for tok in expr:
        if is_num(tok):
            stack.append(float(tok))
        elif is_op(tok):
            res = 0
            if tok == 'u-' or tok == 'u+':
                op = stack.pop()
                if tok == 'u-':
                    res = -op
                elif tok == 'u+':
                    res = op
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if (tok == '&' or tok == '%' or tok == '/') and op1 == 0.0:
                    raise CalcError('На ноль делить нельзя')
                elif tok == '+':
                    res = op1 + op2
                elif tok == '-':
                    res = op2 - op1
                elif tok == '#':
                    res = op2 ** op1
                elif tok == '*':
                    res = op1 * op2
                else:
                    if ((tok == '&' or tok == '%') and
                            (op2 % 1 != 0 or op1 % 1 != 0)):
                        raise CalcError(f'Операция не может быть выполнена,'
                                        f' так как {op2} или {op1} нецелое число')
                    else:
                        if tok == '&':
                            res = int(op2 // op1)
                        elif tok == '/':
                            res = op2 / op1
                        else:
                            res = op2 % op1
            stack.append(res)
    res = stack.pop()
    if res % 1 == 0:
        res = int(res)
    print(res)
    return res
