# Variables
Variables are an important part of programming, and in ErrorScript it is no different. ErrorScript handles variables similar to other langauges, with the difference that it has dynamic typing.

## Variable Declaration
Declaring a variable or constant in ErrorScript is similar to how it is in JavaScript. ErrorScript's syntax uses the `let` keyword for variables and `const` for constants.

Example:
````javascript
let foo = "foo" // Declares variable 'foo' as a string

const bar = "bar" // Declares constant 'bar' as a string
````

Additionally, variables can be declared with a null value by adding a semicolon `;` after the variable name in place of an equals sign `=`, however the same is not true for constants and doing so will result in a `ParseError`.

Example:

````javascript
let this_is_valid; // This is valid, as it is a variable and it can be re-assigned any time

const this_is_invalid; // This is invalid, as it is a constant and its value cannot be changed
````

## Variables vs Constants
Variables and constants are mostly the same, but they also have some differences.

### Variables
* Variables can be declared with a null value
* Variables can be re-assigned at a later time

### Constants
* Constants cannot be declared with a null value
* Constants are constant, meaning they cannot be re-assigned after they have been declared


