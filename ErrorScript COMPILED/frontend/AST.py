# Abstract Syntax Tree

class NodeType:
    Statement = 'stmt'

    Expression = 'expr'

    Program = 'program'

    NumericLiteral = 'numericliteral'
    StringLiteral = 'stringliteral'
    Identifier = 'identifier'

    BinaryExpression = 'binaryexpr'

    VariableDeclaration = 'vardeclaration'
    AssignmentExpression = 'assignmentexpr'


class Statement:
    node_type = NodeType.Statement


class Expression( Statement ):
    node_type = NodeType.Expression


class Program( Statement ):
    node_type = NodeType.Program
    body : list[Statement] = []

    def __repr__( self ) -> str:
        return f"{{ node_type: {self.node_type}, body: {self.body} }}"


class NumericLiteral( Expression ):
    node_type = NodeType.NumericLiteral
    value : float

    def __init__( self, value : float ) -> None:
        self.value = value
    
    def __repr__( self ) -> str:
        return f"{{ node_type: {self.node_type}, value: {self.value} }}"


class StringLiteral( Expression ):
    node_type = NodeType.StringLiteral
    value : str

    def __init__( self, value : str ) -> None:
        self.value = value
    
    def __repr__( self ) -> str:
        return f"""{{ node_type: {self.node_type}, value: "{self.value}" }}"""


class Identifier( Expression ):
    node_type = NodeType.Identifier
    symbol : str

    def __init__( self, symbol : str ) -> None:
        self.symbol = symbol
    
    def __repr__( self ) -> str:
        return f"{{ node_type: {self.node_type}, symbol: {self.symbol} }}"


class BinaryExpression( Expression ):
    node_type = NodeType.BinaryExpression
    left : Expression
    right : Expression
    operator : str

    def __init__( self, left : Expression, right : Expression, operator : str ) -> None:
        self.left = left
        self.right = right
        self.operator = operator
    
    def __repr__( self ) -> str:
        return f"{{ node_type: {self.node_type}, left: {self.left}, right: {self.right}, op: {self.operator} }}"


class VariableDeclaration( Expression ):
    node_type = NodeType.VariableDeclaration
    
    is_const : bool
    identifier : str
    value : Expression = None

    def __init__( self, identifier : str, value : Expression, is_const : bool ) -> None:
        self.identifier = identifier
        self.value = value
        self.is_const = is_const
    
    def __repr__( self ) -> str:
        return f"{{ node_type: {self.node_type}, is_const: {self.is_const}, identifier: {self.identifier}, value: {self.value} }}"


class AssignmentExpression( Expression ):
    node_type = NodeType.AssignmentExpression

    assignee : Expression = None
    value : Expression = None

    def __init__( self, assignee : Expression, value : Expression ) -> None:
        self.assignee = assignee
        self.value = value
    
    def __repr__( self ) -> str:
        return f"{{ node_type: {self.node_type}, assignee: {self.assignee}, value: {self.value} }}"

