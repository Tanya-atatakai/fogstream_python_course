"""
Функция = объект
"""
test_str = 'мы кодеры'


def scream(word):
    assert isinstance(word, str)
    return word.capitalize() + '!!'


print(scream(test_str))
shout = scream

del scream

try:
    scream(test_str)
except NameError as ex:
    print(ex)  # name 'scream' is not defined

print(shout('мы правда кодеры'))


# ====================================

def talk():
    def whisper(word=test_str):
        return word.lower() + '...'

    def scream(word):
        return word.capitalize() + '!!'

    print(whisper())


talk()
