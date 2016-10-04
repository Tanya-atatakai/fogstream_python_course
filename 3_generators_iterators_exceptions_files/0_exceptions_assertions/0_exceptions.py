import sys

my_list = range(7)


def index_error():
    # Обращение по несуществующему индексу
    try:
        element = my_list[9]
    except IndexError as exception:
        print(exception)


def get_user_number():
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


def getting_many_exceptions():
    try:
        f = open('bad_file_for_exceptions.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    except ValueError:
        print("Could not convert data to an integer.")
    except Exception:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    print ('Я выполнилась')


def raising_exceptions():
    # try:
    raise Exception('Привет!', 'Я - ваше первое исключение!')
    # except Exception:
    #     print('Словили исключение. Но почти не обработали. Не надо так')


class MyCustomError(Exception):
    def __init__(self, *args, **kwargs):
        super(MyCustomError, self).__init__(*args, **kwargs)
        print('Кажется, что-то пошло не так..')


def custom_error(x):
    try:
        if x is not 0:
            raise MyCustomError('Моя ошибочка')
        else:
            print('х = 0')
    except MyCustomError as ex:
        raise


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Деление на ноль!!!")
    else:
        print("Результат", result)
    finally:
        y += 1
        divide(x, y)
        print("Все, закончили считать")


# index_error()
# get_user_number()
# getting_many_exceptions()
# raising_exceptions()
custom_error(0)

# divide(2, 1)
# divide(2, 0)
# divide("2", "1")
