# CPSC354

Name: Manuel Pangelinan    
Course: CPSC 354 – Programming Languages  
Semester: Fall 2026

# Programming Assignment 1 – Calculator

This assignment involves implementing a calculator in Python using the Lark parser library. The calculator uses a context-free grammar (CFG) to parse arithmetic expressions, converts them into abstract syntax trees (ASTs), and recursively evaluates them.

# Features
- Addition and subtraction
- Multiplication
- Unary negation
- Exponentiation
- Logarithms
- Parentheses and operator precedence

# Running the Calculator

Install the required dependency:

- python -m pip install lark

Navigate to the assignment directory

Run the calculator as a command-line argument:

- python calculator_cfg.py "1+2*3"

Expected output:

- 7.0

# Documentation

Detailed explanation is in specs.md under the Assignment1 folder

# References

- Starter Code from Professor's repository
- Instructions from assignment

# Programming Assignment 2 – Interpreter

This assignment uses Python and Lark to interpret expressions in the untyped lambda calculus. The interpreter parses each expression into an abstract syntax tree (AST), then uses normal-order evaluation to reduce it.

#Features
- Reduces the leftmost, outermost application first.
- Reduces expressions inside lambda bodies and arguments when needed.
- Uses capture-avoiding substitution to keep free variables from becoming bound.
- Prints the final result to the terminal.

# Running the Interpreter
From the repository root, install Lark and open the assignment folder:

- python -m pip install lark==1.1.9
- cd Assignment2

Pass a lambda expression as a command-line argument:

- python interpreter.py '(\x.x) a'

Expected output:

- a

To check reduction inside a lambda body, run:

- python interpreter.py '\z.(\x.x) y'

Expected output:

- (\z.y)

# References

- lambdaC-2024 starter code
- Programming Assignment 2 handout
