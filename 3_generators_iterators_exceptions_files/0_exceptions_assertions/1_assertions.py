import sys

my_list = range(7)


def divide(x, y):
    assert isinstance(x, int)
    assert isinstance(y, int), 'Вообще то надо чтоб Y был целочисленным'
    return x / y

divide_result = divide(5, 'Конь')