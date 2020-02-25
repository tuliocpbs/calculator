from src.models.operation import CalculatorResult


def test_sum_function():
    calc = CalculatorResult(function='sum', arguments=[1,-2,3])
    assert calc.result == 2
    assert calc.msg == 'Executed with success'


def test_subtract_function():
    calc = CalculatorResult(function='subtract', arguments=[1,-2,3])
    assert calc.result == 0
    assert calc.msg == 'Executed with success'


def test_multiply_function():
    calc = CalculatorResult(function='multiply', arguments=[1,-2,3])
    assert calc.result == -6
    assert calc.msg == 'Executed with success'


def test_divide_function():
    calc = CalculatorResult(function='divide', arguments=[6,2,3])
    assert calc.result == 1
    assert calc.msg == 'Executed with success'


def test_divide_function_division_by_zero():
    calc = CalculatorResult(function='divide', arguments=[1,0,1])
    assert calc.result == None
    assert calc.msg == "Operation failed, error ZeroDivisionError('float division by zero')"
