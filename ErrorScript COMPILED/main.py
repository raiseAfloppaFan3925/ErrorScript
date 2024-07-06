from frontend.parser import Parser
from runtime.interpreter import evaluate
from runtime.environment import Scope, create_GlobalScope



def errorscript():
    parser = Parser()
    GlobalScope = create_GlobalScope()

    print( '' )
    print( '  ████████████████████  ' )
    print( '  █|}█\/██████████████  ' )
    print( '  █|██/███████████████  ' )
    print( '  ████████████████████  ' )
    print( '  ███████|||||██     █  ' )
    print( '  ███████|██████ █████  ' )
    print( '  ███████|||||██     █  ' )
    print( '  ███████|██████████ █  ' )
    print( '  ███████|||||██     █  ' )
    print( '' )
    print( 'ErrorScript v0.8' )

    file = open( "test.err" )
    source_code = file.read()

    program = parser.constructAST( source_code )

    result = evaluate( program, GlobalScope )

    print( result )

    






errorscript()



