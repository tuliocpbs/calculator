from schematics.models import Model
from schematics.types import StringType, IntType
from schematics.types.compound import DictType, ModelType, ListType
from schematics.exceptions import ValidationError


def verify_functions(function):
    if function not in ['sum', 'subtract', 'divide', 'multiply']:
        raise ValidationError('Function not implemented or invalid')

    return function


class CalculatorArgs(Model):
    function=StringType(required=True, validators=[verify_functions])
    arguments=ListType(field=IntType(), required=True)
