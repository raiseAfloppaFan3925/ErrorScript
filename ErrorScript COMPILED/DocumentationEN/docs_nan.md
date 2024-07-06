# NaN
**NaN** is a special case of floating-point numbers that arises when the user tries to do an invalid operation like `0 / 0`. In [ErrorScript](docs_main.md), **NaN**s are treated as a separate type from [float](docs_float.md)s that behave totally differently from what one might expect.

## Operators

### [`NaN`](docs_nan.md) == equals
* Always returns **false**, even if both sides are of type **NaN**.

### [`NaN`](docs_nan.md) != not equals
* Always returns **false**, even if both sides are of type **NaN**.

### [`NaN`](docs_nan.md) > greater than
* Always returns **false**, even if both sides are of type **NaN**.

### [`NaN`](docs_nan.md) < less than
* Always returns **false**, even if both sides are of type **NaN**.

### [`NaN`](docs_nan.md) + addition
* Returns a **NaN**.

### [`NaN`](docs_nan.md) - subtraction
* Returns a **NaN**.

### [`NaN`](docs_nan.md) * multiplication
* Returns a **NaN**.

### [`NaN`](docs_nan.md) / division
* Returns a **NaN**.
