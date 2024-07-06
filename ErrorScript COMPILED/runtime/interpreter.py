from runtime.values import ValueType, RuntimeVal, NullVal, NumberVal, InfinityVal, NaNVal, StringVal, BooleanVal
from frontend.AST import NodeType, Statement, Expression, Program, BinaryExpression, Identifier
from runtime.evaluations.eval_expressions import evaluate_binary_expression, evaluate_numeric_binary_expression, evaluate_string_binary_expression, evaluate_identifier, evaluate_assignment_expression
from runtime.evaluations.eval_statements import evaluate_program, evaluate_variable_declaration
from runtime.environment import Scope








def evaluate( ASTNode : Statement, scope : Scope ) -> RuntimeVal:
    
    match ASTNode.node_type:
        case NodeType.Program:
            return evaluate_program( ASTNode, scope )
        case NodeType.NumericLiteral:
            return NumberVal( ASTNode.value )
        case NodeType.StringLiteral:
            return StringVal( ASTNode.value )
        case NodeType.Identifier:
            return evaluate_identifier( ASTNode, scope )
        case NodeType.BinaryExpression:
            return evaluate_binary_expression( ASTNode, scope )
        case NodeType.VariableDeclaration:
            return evaluate_variable_declaration( ASTNode, scope )
        case NodeType.AssignmentExpression:
            return evaluate_assignment_expression( ASTNode, scope )
        
    
    print( f"Runtime Error: Unexpected ASTNode recieved. -> {ASTNode}" )
    exit()


