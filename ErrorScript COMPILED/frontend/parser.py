from frontend.lexer import TokenType, Token, tokenize
from frontend.AST import NodeType, Statement, Expression, Program, NumericLiteral, StringLiteral, Identifier, BinaryExpression, VariableDeclaration, AssignmentExpression


class Parser:

    tokens : list[Token]

    
    def constructAST( self, source_code : str ):
        self.tokens = tokenize( source_code )

        program = Program()

        while self.not_eof():
            program.body.append( self.parse_statement() )
        
        return program
    

    def parse_statement( self ) -> Statement:
        match self.at().token_type:
            case TokenType.VarDeclaration:
                return self.parse_var_declaration()
            case TokenType.ConstDeclaration:
                return self.parse_var_declaration()
        return self.parse_expression()


    def parse_expression( self ) -> Expression:
        left = self.parse_additive_expression()

        if self.at().token_type == TokenType.EqualsOperator:
            self.eat()
            value = self.parse_additive_expression()
            
            return AssignmentExpression( left, value )
        
        return left


    def parse_assignment_expression( self ) -> Expression:
        pass


    def parse_additive_expression( self ) -> Expression:
        left = self.parse_multiplicative_expression()

        while self.at().value in ['+', '-']:
            operator = self.eat().value
            right = self.parse_multiplicative_expression()
            left = BinaryExpression( left, right, operator )
        
        return left


    def parse_multiplicative_expression( self ) -> Expression:
        left = self.parse_primary_expression()

        while self.at().value in ['*', '/', '%']:
            operator = self.eat().value
            right = self.parse_primary_expression()
            left = BinaryExpression( left, right, operator )
        
        return left


    def parse_var_declaration( self ) -> Expression:
        is_constant = self.eat().token_type == TokenType.ConstDeclaration

        identifier = self.expect( TokenType.Identifier, f"Parse Error: Expected variable name after '{'const' if is_constant else 'let'}' statement.").value

        if self.at().token_type == TokenType.Semicolon:
            self.eat()
            if is_constant:
                print( f"Parse Error: Constants must be declared with a value." )
                exit()
            return VariableDeclaration( identifier, None, is_constant )
        
        self.expect( TokenType.EqualsOperator, f"Parse Error: Expected equals sign (=) after variable identifier" )
        
        value = self.parse_expression()

        return VariableDeclaration( identifier, value, is_constant )


    def parse_primary_expression( self ) -> Expression:
        token_type = self.at().token_type

        match token_type:
            case TokenType.Identifier:
                return Identifier( self.eat().value )
            case TokenType.NumericLiteral:
                return NumericLiteral( float( self.eat().value ) )
            case TokenType.StringLiteral:
                return StringLiteral( self.eat().value )
            case TokenType.OpenParen:
                self.eat()
                value = self.parse_expression()
                self.expect( TokenType.CloseParen, f"Parse Error at line {self.at().line_n}: Expected closing parenthesis ')'." )
                return value
            
            
            
        
        print( f"Parse Error at line {self.at().line_n}: Unexpected token found during parsing: {self.at()}" )
        exit()


    def not_eof( self ):
        return self.tokens[0].token_type != TokenType.EOF

    
    def at( self ):
        return self.tokens[0]
    

    def eat( self ):
        return self.tokens.pop( 0 )
    

    def expect( self, expected_type : TokenType, error_message : str ):
        if self.at().token_type == expected_type:
            return self.tokens.pop( 0 )
        print( error_message )
        exit()