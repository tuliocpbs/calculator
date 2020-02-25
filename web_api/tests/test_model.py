import pytest
from schematics.exceptions import ValidationError

from src.models.models import verify_functions

def test_validate_sum_function():
    assert verify_functions('sum') == 'sum'

def test_validate_subtract_function():
    assert verify_functions('subtract') == 'subtract'

def test_validate_multiply_function():
    assert verify_functions('multiply') == 'multiply'

def test_validate_divide_function():
    assert verify_functions('divide') == 'divide'

def test_invalidate_square_function():
    with pytest.raises(ValidationError):
        verify_functions('square')

def test_invalidate_power_function():
    with pytest.raises(ValidationError):
        verify_functions('power')
