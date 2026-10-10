# Programming Assignment 1 – Calculator Specifications

# 1. Program Overview

This program implements a calculator in Python using the Lark parser library, supporting addition, subtraction, multiplication, exponentiation, unary negation, logarithms, and parentheses.

The calculator takes an arithmetic expression as a command-line argument, parses it using a context-free grammar, converts the resulting parse tree into an abstract syntax tree, and recursively evaluates the AST to produce the final result.

# 2. Context-Free Grammar

The grammar is defined in grammar.lark. It separates arithmetic operations into different grammar levels to enforce operator precedence and associativity.

The order of operations, from lowest to highest precedence, is:

1. Addition (`+`) and binary subtraction (`-`)
2. Multiplication (`*`)
3. Unary negation (`-`)
4. Exponentiation (`^`)
5. Logarithms (`log ... base ...`)
6. Parentheses and numbers

Addition, binary subtraction, and multiplication are left-associative. Exponentiation is right-associative.

Parentheses can override the normal precedence rules.

# 3. Parser and AST Construction

The program reads the grammar from grammar.lark and creates a Lark parser using the LALR parsing algorithm.

The CalcTransformer class inherits from Lark's Transformer class and converts the parse tree into nested Python tuples representing the AST.

Each method corresponds to a specific arithmetic operation:

- plus(items): Creates an addition AST node containing two operands.
- minus(items): Creates a binary subtraction AST node containing two operands.
- times(items): Creates a multiplication AST node containing two operands.
- neg(items): Creates a unary negation AST node containing one operand.
- pow(items): Creates an exponentiation AST node containing a base and exponent.
- log(items): Creates a logarithm AST node containing an argument and base.
- num(items): Converts a numeric token into a floating-point value and creates a number AST node.

The AST represents the structure of the expression without unnecessary concrete syntax such as parentheses.

# 4. Recursive Evaluation

The evaluate(ast) function recursively computes the value of an AST.

Examines the operation stored in the first element of each tuple and evaluates the child expressions.

- plus: Adds two evaluated operands.
- minus: Subtracts the right operand from the left operand.
- times: Multiplies two evaluated operands.
- neg: Negates the evaluated operand.
- pow: Raises the evaluated base to the evaluated exponent.
- log: Uses math.log() to compute the logarithm with the specified base.
- num: Returns the numeric value directly.

An unknown operation raises a ValueError.

# 5. Program Flow

1. Read the grammar from grammar.lark.
2. Initialize the Lark parser using the LALR algorithm.
3. Read the arithmetic expression from the argument.
4. Parse the input expression into a CST.
5. Use CalcTransformer to construct an AST.
6. Recursively evaluate the AST using evaluate(ast).
7. Print the result.

# 6. Testing

The implementation is tested using the arithmetic expressions provided.

The tests verify arithmetic operations, parentheses, unary negation, exponentiation associativity, logarithms, and operator precedence.

- 1+2*3 evaluates to 7
- 2-(4+2) evaluates to -4
- --1 evaluates to 1
- 2^3^2 evaluates to 512
- log 8 base 2 + 1 evaluates to 4
- -3^2 evaluates to -9

The calculator assumes valid input expressions according to the grammar.