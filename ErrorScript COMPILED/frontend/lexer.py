

class TokenType:
    NumericLiteral = 0
    StringLiteral = 1
    
    Identifier = 2

    VarDeclaration = 3
    ConstDeclaration = 4
    EqualsOperator = 5
    Semicolon = 6
    Colon = 7
    Comma = 8
    Period = 9

    BinaryOperator = 10

    OpenParen = 11
    CloseParen = 12
    OpenBracket = 13
    CloseBracket = 14
    OpenBrace = 15
    CloseBrace = 16
    
    Comment = -9
    EOF = -10



class Token:
    token_type : TokenType
    value : str
    line_n : int

    def __init__( self, token_type : TokenType, value : str, line_n : int ):
        self.token_type = token_type
        self.value = value
        self.line_n = line_n
    
    def __repr__( self ):
        return f"{{ type: {self.token_type}, value: {self.value} }}"



KEYWORDS : dict = {
    'let' : TokenType.VarDeclaration,
    'const' : TokenType.ConstDeclaration
}


def tokenize( source_code : str ):
    tokens : list[Token] = []
    
    src : list[str] = list( source_code )

    line_n = 1
    while len( src ) > 0:
        if src[0] in ['+', '-', '*', '/', '%']:
            operator = src.pop( 0 )
            is_comment = False
            if len( src ) > 0:
                if src[0] == '/':
                    is_comment = True
                    comment = '/'
                    while len( src ) > 0 and src[0] != '\n':
                        comment += src.pop( 0 )
                    #tokens.append( Token( TokenType.Comment, comment ) )
            
            if is_comment == False:
                tokens.append( Token( TokenType.BinaryOperator, operator, line_n ) )
        elif src[0] == '=':
            tokens.append( Token( TokenType.EqualsOperator, src.pop( 0 ), line_n ) )
        elif src[0] == ';':
            tokens.append( Token( TokenType.Semicolon, src.pop( 0 ), line_n ) )
        elif src[0] == '(':
            tokens.append( Token( TokenType.OpenParen, src.pop( 0 ), line_n ) )
        elif src[0] == ')':
            tokens.append( Token( TokenType.CloseParen, src.pop( 0 ), line_n ) )
        elif src[0] == '[':
            tokens.append( Token( TokenType.OpenBracket, src.pop( 0 ), line_n ) )
        elif src[0] == ']':
            tokens.append( Token( TokenType.CloseBracket, src.pop( 0 ), line_n ) )
        elif src[0] == '{':
            tokens.append( Token( TokenType.OpenBrace, src.pop( 0 ), line_n ) )
        elif src[0] == '}':
            tokens.append( Token( TokenType.CloseBrace, src.pop( 0 ), line_n ) )
        elif is_num( src[0] ):
            number = src.pop( 0 )

            deci_counter = 1 if number == '.' else 0
            while len( src ) > 0 and is_num( src[0] ):
                if src[0] == '.':
                    deci_counter += 1
                    
                    if deci_counter > 1:
                        print( f"Lexing error at line {line_n}: Numbers cannot have more than one decimal point." )
                        exit()
                number += src.pop( 0 )
                    
            
            tokens.append( Token( TokenType.NumericLiteral, number, line_n ) )
        elif src[0] in [f'"' or f"'"]:
            string_delimiter = src.pop( 0 )
            string = ''

            while len( src ) > 0 and src[0] != string_delimiter:
                string += src.pop( 0 )
            
            if len( src ) == 0:
                print( f"Lexing error at line {line_n}: Unterminated string detected." )
                exit()
            
            src.pop( 0 )

            tokens.append( Token( TokenType.StringLiteral, string, line_n ) )
        elif is_alpha( src[0] ) or src[0] == '_':
            identifier = src.pop( 0 )

            while len( src ) > 0 and ( is_alpha( src[0] ) or is_num( src[0] ) or src[0] == '_' ):
                identifier += src.pop( 0 )
            
            
            reserved = KEYWORDS.get( identifier, "__NULL__" )
            if reserved == "__NULL__":
                tokens.append( Token( TokenType.Identifier, identifier, line_n ) )
            else:
                tokens.append( Token( reserved, identifier, line_n ) )
        elif is_skippable( src[0] ):
            if src[0] == '\n':
                line_n += 1
            src.pop( 0 )
        else:
            print( f"Lexing error at line {line_n}: Unrecognized token {src[0]}" )
            exit()
    
    tokens.append( Token( TokenType.EOF, 'End of File', 999999999 ) )


    return tokens



def is_num( src : str ):
    return src in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']


def is_alpha( src : str ):
    return src.isalpha()


def is_skippable( src : str ):
    return src in [ ' ', '\t', '\n', '\r' ]


