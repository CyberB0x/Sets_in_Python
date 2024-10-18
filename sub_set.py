# Получение подмножества

# Использование цикла for
my_set = {1, 2, 3, 4, 5, 6}
sub_set = set()

for x in my_set:
    if x % 2 == 0:
        sub_set.add(x)

print(sub_set)

# Использование функции filter()
my_set_1 = {10, 20, 30, 40}
sub_set_filter = set(filter(lambda x: x % 2 == 0, my_set_1))
print(sub_set_filter)


# Вот так можно отобрать только четные элементы из множества
my_set_2 = {1, 2, 6, 7, 9, 8, 5}
result = {x for x in my_set_2 if x % 2 == 0}
print(result)

# А вот так только строки
my_string_set = {1, 2, 3, 4, 5, "Hello", "Apple"}
only_strings = {i for i in my_string_set if type(x) == str}
print(only_strings)

#/////////////////////////////////
# Проверка вложенности множеств
#////////////////////////////////

# Использование оператора <=
set_a = {1, 2, 3, 4, 5}
set_b = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set_a <= set_b)
print(set_b <= set_a)

# Использование метода issubset()
set_c = {1, 2, 3, 4, 5, 6}
set_d = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(set_c.issubset(set_d))
print(set_d.issubset(set_c))

#--------------------------
# Проверка на надмножество
#--------------------------

# Использование оператора >=
set_e = {1, 2, 3, 4, 5}
set_f = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set_e >= set_f)
print(set_f >= set_e)

# Использование метода issuperset()
set_h = {1, 2, 3, 4, 5}
set_j = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set_e.issuperset(set_f))
print(set_f.issuperset(set_e))