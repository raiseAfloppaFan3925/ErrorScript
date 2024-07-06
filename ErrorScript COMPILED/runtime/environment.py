from runtime.values import ValueType, RuntimeVal, NullVal, NumberVal, InfinityVal, NaNVal, StringVal, BooleanVal



class Scope:
    
    parent = None
    variables : dict = {}
    constants : list[str] = []

    def __init__( self, parent ) -> None:
        self.parent = parent
    

    def declare_var( self, var_name : str, value : RuntimeVal, is_const : bool ) -> RuntimeVal:
        reserved = self.variables.get( var_name, "____NULL____" )
        if reserved != "____NULL____":
            print( f"Runtime Error: Cannot declare variable {var_name} as it already exists." )
        
        if is_const:
            self.constants.append( var_name )
        self.variables.update( { var_name : value } )

        return value
    

    def assign_var( self, var_name : str, value : RuntimeVal ) -> RuntimeVal:
        scope = self.resolve( var_name )
        if var_name in scope.constants:
            print( f"Runtime Error: Cannot re-assign constant {var_name} as it is a constant." )
            exit()
        scope.variables[var_name] = value

        return value
    

    def get_var( self, var_name : str ) -> RuntimeVal:
        scope = self.resolve( var_name )
        
        return scope.variables[var_name]


    def resolve( self, var_name : str ):
        reserved = self.variables.get( var_name, "____NULL____" )

        if reserved != "____NULL____":
            return self
        
        if self.parent == None:
            print( f"Runtime Error: Could not resolve variable {var_name}.")
            exit()
        
        return self.parent.resolve( var_name )


def create_GlobalScope():
    GlobalScope = Scope( None )

    GlobalScope.declare_var( 'null', NullVal(), True )
    GlobalScope.declare_var( 'true', BooleanVal( True ), True )
    GlobalScope.declare_var( 'false', BooleanVal( False ), True )
    GlobalScope.declare_var( 'NaN', NaNVal(), True )
    GlobalScope.declare_var( 'inf', InfinityVal( 0 ), True )
    GlobalScope.declare_var( 'pi', NumberVal( 3.1415926535897932384626433832795028841971693993751058209749445923078164 ), True )
    GlobalScope.declare_var( 'tau', NumberVal( 6.2831853071795864769252867665590057683943387987502116419498891846156328 ), True )
    GlobalScope.declare_var( 'euler', NumberVal( 2.718281828459045235360287471352662497757247093699959574966967627724076 ), True )
        

    return GlobalScope



