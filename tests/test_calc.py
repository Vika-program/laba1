import pytest
from src.other import CalcError
from src.calc import calc


def test_calc():
    assert calc("(1) + (2) * (3)") == 7
    assert calc("1 + 3") == 4
    assert calc('-2 ** (88 / 11)') == 256
    assert calc("((1 + 2) * ((-2) + 4 ** 2) // 7)") == 6
    assert calc("(((1 + 4) // 2) ** 3) % 3") == 2
    assert calc('(123 + 345) / 23') == 20.347826086956523
    assert calc("23.5 + 45.2") == 68.7
    assert calc("25.5 / 2") == 12.75
    assert calc("(12.25 + 24.67) * 2") == 73.84
    assert calc('2.5 ** 2') == 6.25
    assert calc("(100 + 56) * 2 % 34") == 6
    assert calc('-(1 + 2) * 3') == -9
    assert calc('2**3**2') == 512
    assert calc('2 + 3 * 4 ** 2 - 10 / 2') == 45
    assert calc('2 ** 3 ** 2 / 4 * 3 + 1') == 385
    assert calc('((2 + 3 * (4 - 1)) ** 2 - 10) // 3 + 5 % 3') == 39

    with pytest.raises(CalcError):
        calc("23.5 // 4.5")
    with pytest.raises(CalcError):
        calc('34.2 % 2')
    with pytest.raises(CalcError):
        calc('')
    with pytest.raises(CalcError):
        calc('1 1 +')
    with pytest.raises(CalcError):
        calc('11 +')
    with pytest.raises(CalcError):
        calc('11 + (3 +)')
    with pytest.raises(CalcError):
        calc("2 (* 3)")
    with pytest.raises(CalcError):
        calc("1 + + 3")
    with pytest.raises(CalcError):
        calc("(1)) + (2")
    with pytest.raises(CalcError):
        calc("1 / 0")
    with pytest.raises(CalcError):
        calc("w")
    with pytest.raises(CalcError):
        calc("(-45 + 56")
    with pytest.raises(CalcError):
        calc("456 % (20 - 20)")
    with pytest.raises(CalcError):
        calc("((1 + 2)")
    with pytest.raises(CalcError):
        calc("(1 + 2))")
    with pytest.raises(CalcError):
        calc(')1+2(')
    with pytest.raises(CalcError):
        calc('(1 + 2) (2 + 3)')
    with pytest.raises(CalcError):
        calc('*2')
    with pytest.raises(CalcError):
        calc('56 + .56')
    with pytest.raises(CalcError):
        calc('56 46')
