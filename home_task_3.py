import copy

# 1. Создать 3 переменные одного и тоже типа с одинаковыми
# данными и с одинаковыми идентификаторами.
print(1, 50*"-")
var1 = 'test'
var2 = 'test'
var3 = 'test'


# print("var1: ", var1, "Type :", type(var1), "ID: ", id(var1))
# print("var2: ", var2, "Type :", type(var2), "ID: ", id(var2))
# print("var3: ", var3, "Type :", type(var3), "ID: ", id(var3))
print("Equal: ", var1 == var2 == var3)
print("Equal ID: ", var1 is var2 is var3)

# 2. Создать 2 переменные одного и тоже типа с одинаковыми
# данными и с разными идентификаторами.
print(2, 50*"-")
var4 = [1, 2, ('a', 'b', 'c'), 4]
var5 = [1, 2, ('a', 'b', 'c'), 4]

# print("var4: ", var4, "Type :", type(var4), "ID: ", id(var4))
# print("var5: ", var5, "Type :", type(var5), "ID: ", id(var5))
print("Equal: ", var5 == var4)
print("Equal ID: ", var4 is var5)

# 3*. Поменять их типы так, чтобы у 1-х трёх стали разные идентификаторы,
# но при этом остались одинаковые данные
# (и одинаковый тип), а у 2-х последних стали одинаковые идентификаторы
# и остаhome_task_3лись одинаковые данные (и одинаковый тип).
# добиться нужного результата необходимо только приведением типов данных к нужному

print(3, 50*"-")
var1 = list(var1)
var2 = list(var2)
var3 = list(var3)
print("Equal: ", var1 == var2 == var3)
print("Equal ID: ", var1 is var2 is var3)
print(20*"-")

var4 = tuple(var4)
var5 = copy.copy(var4)
print("var4, ", id(var4))
print("var5, ", id(var5))
print("Equal: ", var5 == var4)
print("Equal ID: ", var4 is var5)
print("END", 50*"-")
