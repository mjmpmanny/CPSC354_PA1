import sys
from lark import Lark, Transformer, Tree
import lark
import os

#print(f"Python version: {sys.version}")
#print(f"Lark version: {lark.__version__}")

#  run/execute/interpret source code
def interpret(source_code):
    cst = parser.parse(source_code)
    ast = LambdaCalculusTransformer().transform(cst)
    result_ast = evaluate(ast)
    result = linearize(result_ast)
    return result

# convert concrete syntax to CST
parser = Lark(open("grammar.lark").read(), parser='lalr')

# convert CST to AST
class LambdaCalculusTransformer(Transformer):
    def lam(self, args):
        name, body = args
        return ('lam', str(name), body)

    def app(self, args):
        return ('app', *args)

    def var(self, args):
        token, = args
        return ('var', str(token))

    def NAME(self, token):
        return str(token)

# Take one leftmost-outermost beta step, or return None at normal form.
def reduce_once(tree):
    if tree[0] == 'app':
        _, function, argument = tree
        if function[0] == 'lam':
            _, name, body = function
            return substitute(body, name, argument)

        reduced_function = reduce_once(function)
        if reduced_function is not None:
            return ('app', reduced_function, argument)

        reduced_argument = reduce_once(argument)
        if reduced_argument is not None:
            return ('app', function, reduced_argument)

    elif tree[0] == 'lam':
        _, name, body = tree
        reduced_body = reduce_once(body)
        if reduced_body is not None:
            return ('lam', name, reduced_body)

    return None


def evaluate(tree):
    while True:
        reduced = reduce_once(tree)
        if reduced is None:
            return tree
        tree = reduced

# generate a fresh name 
# needed eg for \y.x [y/x] --> \z.y where z is a fresh name)
class NameGenerator:
    def __init__(self):
        self.counter = 0

    def generate(self):
        self.counter += 1
        # user defined names start with lower case (see the grammar), thus 'Var' is fresh
        return 'Var' + str(self.counter)

name_generator = NameGenerator()

# for beta reduction (capture-avoiding substitution)
# 'replacement' for 'name' in 'tree'
def substitute(tree, name, replacement):
    # tree [replacement/name] = tree with all instances of 'name' replaced by 'replacement'
    if tree[0] == 'var':
        if tree[1] == name:
            return replacement # n [r/n] --> r
        else:
            return tree # x [r/n] --> x
    elif tree[0] == 'lam':
        if tree[1] == name:
            return tree # \n.e [r/n] --> \n.e
        else:
            fresh_name = name_generator.generate()
            return ('lam', fresh_name, substitute(substitute(tree[2], tree[1], ('var', fresh_name)), name, replacement))
            # \x.e [r/n] --> (\fresh.(e[fresh/x])) [r/n]
    elif tree[0] == 'app':
        return ('app', substitute(tree[1], name, replacement), substitute(tree[2], name, replacement))
    else:
        raise Exception('Unknown tree', tree)

def linearize(ast):
    if ast[0] == 'var':
        return ast[1]
    elif ast[0] == 'lam':
        return "(" + "\\" + ast[1] + "." + linearize(ast[2]) + ")"
    elif ast[0] == 'app':
        return "(" + linearize(ast[1]) + " " + linearize(ast[2]) + ")"
    else:
        return ast

def main():
    import sys
    if len(sys.argv) != 2:
        #print("Usage: python interpreter.py <filename or expression>", file=sys.stderr)
        sys.exit(1)

    input_arg = sys.argv[1]

    if os.path.isfile(input_arg):
        # If the input is a valid file path, read from the file
        with open(input_arg, 'r') as file:
            expression = file.read()
    else:
        # Otherwise, treat the input as a direct expression
        expression = input_arg

    result = interpret(expression)
    print(result)

if __name__ == "__main__":
    main()
