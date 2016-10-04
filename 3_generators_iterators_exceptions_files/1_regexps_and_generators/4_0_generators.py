def make_counter(x):
    print('entering make_counter')
    y = 99
    while True:
        yield x, y
        print('incrementing x')
        x += 1
        if x > 7:
            yield y
            # raise StopIteration


counter = make_counter(2)
counter_new = counter
print('---')
print(next(counter))
print(next(counter))
print(next(counter))
del counter
print(next(counter_new))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
