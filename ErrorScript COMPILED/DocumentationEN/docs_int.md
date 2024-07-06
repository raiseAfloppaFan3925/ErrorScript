# int
The **int** datatype is an integer datatype that stores whole numbers.

**int**s can be automatically converted into [float](docs_float.md)s when necesarry, and the same goes the other way around.

## Operators

### [`int`](docs_int.md) + addition
* Adds the two numbers together.\
 **Note: If the other side is a [float](docs_float.md), then the result is a float.**

 Example:
 ````js
 let a = 1
 let b = 1

 let c = pi // 'pi' is a built-in constant with a value of '3.141592653589793'.
 let d = 20

 print( a + b ) // Prints '2'
 print( c + d ) // Prints '23.141592653589793'
 ````

---

### [`int`](docs_int.md) - subtraction
* Subtracts the right number from the left number.\
**Note: If the other side is a [float](docs_float.md), then the result is a float.**
 Example:
 ````js
 let a = 200
 let b = 123

 print( a - b ) // Prints '77'
 ````

---

### [`int`](docs_int.md) * multiplication
* Multiplies the two **int**s.\
**Note: If the other side is a [float](docs_float.md), then the result is a float.**
 Example:
 ````js
 let a = 250
 let b = 2.0

 print( a * b ) // Returns '500'
 ````

---

### [`int`](docs_int.md) / division
* Divides the left number by the right number.\
 **Note: If the right side is also an int, divison will result in integer division happening. Integer division takes the quotient and floors it.**

 Example:
 ````js
 let a = 1
 let b = 3

 print( a / b ) // Prints '0', as both operands are ints and the floor of 0.3333... is 0

 let c = 5.0
 let d = 2

 print( c / d ) // Prints '2.5', as one of the operands is a float.
 ````

