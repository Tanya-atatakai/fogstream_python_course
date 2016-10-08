"""
Дескрипторы
"""
class ClassA:
    var = 100500


class ClassB:
    name = 'Борис'


a, b = ClassA(), ClassB()

a.var
# 100500
getattr(a, 'var')  # ?
getattr(a, 'other_var', None)  # ?
getattr(a, 'another_var', 33)  # ?

a.x = 1
print(a.x)  # ?
setattr(a, 'x', 'XXX')
print(a.x)  # ?

del a.x
delattr(a, 'x')

"""
Дескрипторы setattr и delattr взаимодействуют только с самим объектом a,
а точнее - с a.__dict__
"""


class MyDescriptor:
    def __getattr__(self, item):
        return "MyValue"


desc = MyDescriptor()
desc.aaa
# MyValue
