def simple_tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name))

        return func_wrapper

    return tags_decorator



@simple_tags("div")
@simple_tags("p")
def get_text(name):
    return "Hello " + name


print(get_text("Ваня"))


class A:
    @property
    def var(self):
        return self._var



a = A()
a.var = 33


def tags(tag_name):
    def tags_decorator(func):
        def func_wrapper(*args, **kwargs):
            return "<{0}>{1}</{0}>".format(tag_name, func(*args, **kwargs))

        return func_wrapper

    return tags_decorator


@tags('p')
def many_args_test(*args, **kwargs):
    return ', '.join(args)


print(many_args_test('Petr', 'SuperIvan'))
