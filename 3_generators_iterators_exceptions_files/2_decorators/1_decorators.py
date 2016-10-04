def get_text(name):
    return "Что же ты, {0}, пригорюнился".format(name)


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))

    return func_wrapper


def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))

    return func_wrapper


my_get_text = div_decorate(p_decorate(get_text))


@p_decorate
@div_decorate
def build_text(name):
    return 'Вот снова ты грустный, {}'.format(name)


print(build_text('Света'))
