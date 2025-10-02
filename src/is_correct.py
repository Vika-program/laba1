import re
from src.other import is_num
def is_correct(expr):
    """проверяет корректность введённого математического выражения
    :param expr: математическое выражение в обычной записи (с уже произведённой заменой ** на # и // на &)
    :return: возвращает истину или ложь"""
    num = fr"\(*(?:\(\s*[+-])?\s*\d+(?:.\d+)?\s*\)*"
    op = fr"\s*[-#&+%*/]\s*"
    open_brackets = 0
    for symb in expr:
        if symb == '(':
            open_brackets += 1
        elif symb == ')':
            open_brackets -= 1
        if open_brackets < 0:
            return False
    if is_num(expr):
        return True
    if (re.fullmatch(fr'\s*\(*\s*{num}{op}(?:{num}|(?:\s*\(*\s*{num}{op}{num}))'  
                    fr'(?:(?:{op}{num})|(?:{op}\(*\s*{num}{op}{num}))*',expr) #проверяем корректность
            and open_brackets == 0):
        return True
    return False