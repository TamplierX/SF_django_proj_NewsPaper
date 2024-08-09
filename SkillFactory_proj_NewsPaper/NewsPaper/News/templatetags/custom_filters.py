from django import template


register = template.Library()


CENSOR_WORDS = [
    'First', 'first',
    'Second', 'second',
    'Third', 'third'
]


@register.filter()
def censor(text):
    if type(text) is not str:
        raise TypeError('Фильтр "censor" предназначен только для переменных строкового типа ')

    words = text.split()
    result = []
    for word in words:
        if word in CENSOR_WORDS:
            result.append(word[0] + "*" * (len(word) - 2) + word[-1])
        else:
            result.append(word)

    return " ".join(result)

