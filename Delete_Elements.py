# Удаление элементов
# Функции remove() и discard()

# Метод remove()

my_set = {10, 20, 30, 40, 50}
my_set.remove(2)
print(my_set) # Console {10, 30, 40, 50}
# Если элемента нет в множестве, возникает ошибка
my_set.remove(4) # KeyError: 4

#-----------------------------------

# Метод discard()

my_set = {10, 20, 30, 40, 50, 60}
my_set.discard(4)
print(my_set) # Console {10, 20, 30, 50, 60}
# Если элемента нет в множестве, ошибки не будет
my_set.discard(7)
print(my_set) # Console {10, 20, 30, 50, 60}

#-----------------------------------

# Функции pop() и clear()

# Метод pop()
my_set = {1, 2, 3, 4, 5, 6}
remove_elem = my_set.pop()
print(remove_elem) # Вывод: Один из элементов множества, например, 1
print(my_set)
# Если множество пустое, возникает ошибка
empty_set = set()
empty_set.pop() # KeyError: 'pop from an empty set'

# Метод clear()
# Метод clear() удаляет все элементы из множества, делая его пустым.

my_set = {1, 2, 3, 4}
my_set.clear()
print(my_set)

#--------------------------------
# Использование оператора del

"""
Удаление множества

Когда оператор del используется для удаления множества, это множество 
больше не существует, и все его элементы удаляются из памяти
"""

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print("Current set:", my_set)
# Удаление множества
del my_set

# Попытка доступа к удаленному множеству вызовет ошибку
# print(my_set)  # NameError: name 'my_set' is not defined




