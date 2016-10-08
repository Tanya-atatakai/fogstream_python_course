import re


def find_expression(my_string):
    result = re.findall(r'-?[ ]?([0-9]+\.?[0-9]*)[ ]?([\+\-\*/])[ ]?([0-9]+\.?[0-9]*)', my_string)
    return result


def calc_expression(my_string):
    for expr in find_expression(my_string):
        expr_str = ''.join(map(str, expr))
        result = eval(expr_str)
        print("%s = %s" % (expr_str, result))

new_string = input("Введите строку: ")
calc_expression(new_string)
