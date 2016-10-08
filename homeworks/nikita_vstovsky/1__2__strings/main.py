import re


def check_num(char):
    for num in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        if num == char:
            return True
    return False


def check_long_num(my_string):
    if len(my_string) < 3:
        return False

    for char in my_string:
        if not check_num(char):
            return False

    return True


def check_ref(my_string):
    if my_string.find('http://') != 0:
        if my_string.find('https://') != 0:
            return False
    return True


def check_email(my_string):
    parts = my_string.split('@')
    if len(parts) != 2:
        return False

    part1, part2 = parts

    if len(part2) < 3 or '.' not in part2[1:-1]:
        return False

    return True


def capital_first(func_type='regexp'):
    def capital_first_decorator(func):
        def func_wrapper(my_string):
            new_string = func(my_string)
            if func_type == 'regexp':
                return re.sub(r'[a-zа-я]', lambda pat: pat.group(0).upper(), new_string[0]) + re.sub(r'[A-ZА-Я]', lambda pat: pat.group(0).lower(), new_string[1:])
            elif func_type == "func":
                return new_string.capitalize()
            else:
                return new_string

        return func_wrapper
    return capital_first_decorator


def search_references(func_type='regexp'):
    def search_references_decorator(func):
        def func_wrapper(my_string):
            new_string = func(my_string)
            if func_type == 'regexp':
                return re.sub(r"https?://[^\s]+", '[ссылка запрещена]', new_string)
            elif func_type == "func":
                words = new_string.split()
                for i, word in enumerate(words):
                    if check_ref(word):
                        words[i] = '[Ссылка запрещена]'
                return ' '.join(map(str, words))
            else:
                return new_string

        return func_wrapper
    return search_references_decorator


def search_email(func_type='regexp'):
    def search_email_decorator(func):
        def func_wrapper(my_string):
            new_string = func(my_string)
            if func_type == 'regexp':
                return re.sub(r"([a-zA-Z0-9_\.-]+)@([a-zA-Z0-9_\.-]+)\.([a-zA-Z\.]{2,6})",
                              '[Контакты запрещены]',
                              new_string)
            elif func_type == "func":
                words = new_string.split()
                for i, word in enumerate(words):
                    if check_email(word):
                        words[i] = 'Контакты запрещены]'
                return ' '.join(map(str, words))
            else:
                return new_string

        return func_wrapper
    return search_email_decorator


def search_long_num(func_type='regexp'):
    def search_long_num_decorator(func):
        def func_wrapper(my_string):
            new_string = func(my_string)
            if func_type == 'regexp':
                return re.sub(r"[0-9]{3,}", '', new_string)
            elif func_type == "func":
                words = new_string.split()
                for i, word in enumerate(words):
                    if check_long_num(word):
                        words[i] = ''
                return ' '.join(map(str, words))
            else:
                return new_string

        return func_wrapper
    return search_long_num_decorator


@search_long_num('func')
@search_email('func')
@search_references('func')
@capital_first('func')
def get_string(new_string):
    return new_string

new_string = input("Введите строку: ")
print(get_string(new_string))
