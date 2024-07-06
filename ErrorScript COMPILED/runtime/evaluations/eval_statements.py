import runtime.interpreter as interpreter
from runtime.values import ValueType, RuntimeVal, NullVal, NumberVal, StringVal, BooleanVal
from frontend.AST import NodeType, Statement, Program, NumericLiteral, StringLiteral, BinaryExpression, VariableDeclaration
from runtime.environment import Scope




def evaluate_program( ASTNode : Program, scope : Scope ) -> RuntimeVal:
    last_evaluated_node = NullVal()

    for node in ASTNode.body:
        last_evaluated_node = interpreter.evaluate( node, scope )
    
    return last_evaluated_node


def evaluate_variable_declaration( ASTNode : VariableDeclaration, scope : Scope ) -> RuntimeVal:
    value = interpreter.evaluate( ASTNode.value, scope ) if ASTNode.value != None else NullVal()

    return scope.declare_var( ASTNode.identifier, value, ASTNode.is_const )




