
class ValueType:
    Null = 'null'
    Number = 'NumericLiteral'
    String = 'StringLiteral'
    Boolean = 'BooleanLiteral'


class RuntimeVal:
    val_type : ValueType


class NullVal( RuntimeVal ):
    val_type = ValueType.Null
    value : str = 'null'

    def __repr__( self ) -> str:
        return f"{{ value type: {self.val_type}, value: {self.value} }}"


class NumberVal( RuntimeVal ):
    val_type = ValueType.Number
    extra_type : str = 'Number'
    value : float
    
    def __init__( self, value : float ) -> None:
        self.value = value
    
    def __repr__( self ) -> str:
        return f"{{ value type: {self.val_type}, value: {self.value} }}"


class InfinityVal( RuntimeVal ):
    val_type = ValueType.Number
    extra_type = 'Infinity'
    sign : int = 0
    value : str = 'inf'
    
    def __init__( self, sign : int ):
        self.sign = sign

    def __repr__( self ) -> str:
        return f"{{ value type: {self.val_type}, value: {'-' if self.sign == 1 else ''}{self.value} }}"


class NaNVal( RuntimeVal ):
    val_type = ValueType.Number
    extra_type = 'NaN'
    value : str = 'NaN'
    
    def __repr__( self ) -> str:
        return f"{{ value type: {self.val_type}, value: {self.value} }}"



class StringVal( RuntimeVal ):
    val_type = ValueType.String
    value : str
    
    def __init__( self, value : str ) -> None:
        self.value = value
    
    def __repr__( self ) -> str:
        return f"""{{ value type: {self.val_type}, value: "{self.value}" }}"""


class BooleanVal( RuntimeVal ):
    val_type = ValueType.Boolean
    value : bool
    
    def __init__( self, value : bool ) -> None:
        self.value = value
    
    def __repr__( self ) -> str:
        return f"""{{ value type: {self.val_type}, value: {self.value} }}"""



