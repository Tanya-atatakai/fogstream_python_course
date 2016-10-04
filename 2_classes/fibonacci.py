# coding=utf-8

def fib_func(n):
    a = 0
    b = 1
    for i in range(n - 1):
        print(a)
        a, b = b, a + b
    return a


fib_func(15)


class Fib:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib


for item in Fib(15):
    print(item)

print('========')
