def get_even_or_odd_numbers(a, b):
    return list(filter(lambda x: x % 2 == 1-b, range(a)))


def search_words(he, b):
    return list([i for i in filter(lambda a: a.find(he) >= 0, b)])


def flatten(arr):
    yield from [el for item in arr for el in item]


if __name__ == '__main__':
    assert get_even_or_odd_numbers(3, True) == [0, 2]
    assert get_even_or_odd_numbers(4, False) == [1, 3]

    assert search_words('he', ['hello', 'orange', 'phenomenon']) == ['hello', 'phenomenon']
    assert search_words('abc', ['hello', 'orange', 'phenomenon']) == []

    generator = flatten([[1, 2], [], [3, 4, 5]])
    assert next(generator) == 1
    assert next(generator) == 2
    assert next(generator) == 3
    assert next(generator) == 4
    assert next(generator) == 5
