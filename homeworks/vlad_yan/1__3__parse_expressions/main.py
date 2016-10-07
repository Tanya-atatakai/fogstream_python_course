import re
from optparse import OptionParser

# define and compile my regular expression
floatnumber = '\d+(?:\.\d+)?'
myregex = '(?P<operand1>{number})\s*(?P<operation>[\+\-\*/])\s*(?P<operand2>{number})'.format(number=floatnumber)
myre = re.compile(myregex)


def find_expressions(myre_, string):
    """Get all the arithmetic expressions in the string."""
    expressions = myre_.findall(string)

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


def main(myre_, string):
    """Main function."""
    expressions = find_expressions(myre_, string)

    for expr in expressions:
        evaluate_expression(expr)


if __name__ == '__main__':
    parser = OptionParser()
    opts, args = parser.parse_args()

    arg = args[0]
    main(myre, arg)
