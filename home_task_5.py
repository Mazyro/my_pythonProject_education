import random
# choice функція повертає одне значення із ітерованного обєкта
# def get_random_value():
#     return random.choice((1, 2, 3, 4, 5))
# choices функція повертає скільки значень скільк передано в змінній к
# def get_random_values(choices, size=2):
#     return random.choices(choices, k=size)


def retry(attempts=5, desired_value=None):
    desired_value = [] if desired_value is None else desired_value

    def wrapper(func):
        def inner_wrapper(*args, **qwargs):
            for i in range(1, attempts+1):
                res = func(*args, **qwargs)
                # print(res)
                if desired_value == res:
                    res = desired_value
                    print(res, 'on ', i, 'attempt')
                    break
            else:
                res = 'failure'
                print(res)
            return res
        return inner_wrapper
    return wrapper


def print_square(n, level=0):

    if n == level+n:
        print('*' * n)
    if n > 2:
        print('*'+' '*((n-2)+level)+'*')
        print_square(n-1, level+1)
    elif n == 2:
        print('*' * (level+2))


if __name__ == '__main__':

    # examples of implemented 'retry' decorator
    @retry(desired_value=3)
    def get_random_value():
        return random.choice((1, 2, 3, 4, 5))


    @retry(desired_value=[1, 2])
    def get_random_values(choices, size=2):
        return random.choices(choices, k=size)


    @retry(attempts=7, desired_value=3)
    def get_random_value():
        return random.choice((1, 2, 3, 4, 5))


    @retry(attempts=2, desired_value=[1])
    def get_random_values(choices, size=2):
        return random.choices(choices, k=size)


    # examples of function usages
    get_random_value()
    get_random_values([1, 2, 3, 4])
    get_random_values([1, 2, 3, 4])
    get_random_values([1, 2, 3, 4], 3)
    get_random_values([1, 2, 3, 4], size=1)
    print_square(5)
