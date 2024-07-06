import runtime.interpreter as interpreter
from runtime.values import ValueType, RuntimeVal, NullVal, NumberVal, InfinityVal, NaNVal, StringVal, BooleanVal
from frontend.AST import NodeType, Statement, Program, NumericLiteral, StringLiteral, BinaryExpression, Identifier, AssignmentExpression
from runtime.environment import Scope


def evaluate_numeric_binary_expression( left : NumberVal, right : NumberVal, operator : str ) -> RuntimeVal:
    result = None

    match operator:
        case '+':
            result = left.value + right.value
        case '-':
            result = left.value - right.value
        case '*':
            result = left.value * right.value
        case '/':
            if left.extra_type == 'Number' and right.extra_type == 'Number':
                if right.value != 0.0:
                    result = left.value / right.value
                elif left.value != 0.0:
                    if left.value > 0.0:
                        return InfinityVal( 0 )
                    else:
                        return InfinityVal( 1 )
                else:
                    return NaNVal()
            elif right.extra_type == 'Infinity':
                result = 0.0
            elif right.extra_type == 'NaN':
                return NaNVal()
            if left.extra_type == 'Infinity':
                return InfinityVal()
            elif left.extra_type == 'NaN':
                return NaNVal()
            
        case '%':
            result = left.value % right.value


    return NumberVal( result )


def evaluate_string_binary_expression( left : StringVal, right : StringVal, operator : str ) -> RuntimeVal:
    result = None

    match operator:
        case '+':
            result = left.value + right.value
        case _:
            print( 'Runtime Error: Strings only support addition.' )
            exit()
        
    
    return StringVal( result )


def evaluate_binary_expression( expr : BinaryExpression, scope : Scope ) -> RuntimeVal:
    left : RuntimeVal = interpreter.evaluate( expr.left, scope )
    right : RuntimeVal = interpreter.evaluate( expr.right, scope )
    op : str = expr.operator
    
    if left.val_type == ValueType.Number and right.val_type == ValueType.Number:
        return evaluate_numeric_binary_expression( left, right, op )
    if left.val_type == ValueType.String and right.val_type == ValueType.String:
        return evaluate_string_binary_expression( left, right, op )
    
    return NullVal()


def evaluate_identifier( identifier : Identifier, scope : Scope ) -> RuntimeVal:
    value = scope.get_var( identifier.symbol )

    return value


def evaluate_assignment_expression( assignment : AssignmentExpression, scope : Scope ) -> RuntimeVal:
    if assignment.assignee.node_type != NodeType.Identifier:
        print( f"Runtime Error: Cannot assign value to a non-variable." )
        exit()

    value = interpreter.evaluate( assignment.value, scope  )

    return scope.assign_var( assignment.assignee.symbol, value )

    

