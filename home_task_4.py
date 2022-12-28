# визначення більшого числа з двох
# (функція приймає 2 числа та на виході повертає більше);
def number_compare_biggest(a, b):
    if a > b:
        return a
    else:
        return b


print("biggest number among two is - ", number_compare_biggest(150, -150))


# if __name__=='__main__':


# визначення меншого числа з трьох
# (аналогічно до попередньої задачі);

def number_compare_smallest(x, y, z):
    if (x < y) and (x < z):
        return x
    elif (y < x) and (y < z):
        return y
    else:
        return z


print("smallest number among tree is - ", number_compare_smallest(88, 0, -1))


# модуль числа (функція приймає одне значення та повертає його модуль);

def num_module(a):
    if a < 0:
        return a * -1
    else:
        return a


print("module is ", num_module(-555))

# виведення на екран суми значень (функція приймає
# 2 значення та лише виводить їхню суму на екран);


def my_func_suma(x, y):
    suma = x + y
    return suma


print("Sum equal to ", my_func_suma(5, 5))

# виведення на екран словом чи є число позитивним
# (функція приймає 1 значення та виводить на екран
# інформацію про його знак.
# Особливу увагу варто приділити нульовому значенню).


def is_positive(x):

    if (type(x) == int or type(x) == float) and x < 0:
        return "-"
    elif (type(x) == int or type(x) == float) and x > 0:
        return "+"
    elif (type(x) == int or type(x) == float) and x == 0:
        return "без знаку"
    else:
        return "Pls, pass number format"


print("polarity of passed number is: ", is_positive(0))

