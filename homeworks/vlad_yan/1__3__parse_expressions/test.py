import re
from optparse import OptionParser


# define some constants
operations = '[\+\-\*/]'
number = '\s*\d+(?:\.\d+)?\s*'

# define my regular expression
bracket_expr = '\({number}\s*{operations}\s*{number}\)'.\
    format(number=number, operations=operations)
complex_expr = '({number}|{bracket_expr}|{operations})+'.\
    format(number=number, operations=operations, bracket_expr=bracket_expr)


def find_expressions(myre, string):
    """Get all the arithmetic expressions in the string."""
    expressions = re.findall(myre, string)

    return expressions


def evaluate_expression(expression):
    """Evaluate arithmetic expression and return the result."""
    operand1, operation, operand2 = expression
    operand1 = float(operand1)
    operand2 = float(operand2)

    if operation == '+':
        result = operand1 + operand2
    elif operation == '-':
        result = operand1 - operand2
    elif operation == '*':
        result = operand1 * operand2
    elif operation == '/':
        result = operand1 / operand2
    else:
        print 'ERROR: unknown operation!'
        return

    expr_str = ''.join(expression)
    print '%s = %s' % (expr_str, result)


def main(myre, string):
    """Main function."""
    expressions = find_expressions(myre, string)

    for expr in expressions:
        evaluate_expression(expr)


if __name__ == '__main__':
    parser = OptionParser()
    opts, args = parser.parse_args()

    arg = args[0]
    main(complex_expr, arg)
