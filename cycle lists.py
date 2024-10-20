# Циклы по списку

# Цикл for
my_fruit_list = ["Apple", "Cherry", "Peach"]
for fruit in my_fruit_list:
    print(fruit)

#------------------------
"""Обход списка в обратном 
порядке можно реализовать с помощью срезов"""
#------------------------
my_fruits = ["Apple", "Peach", "Banana"]
for fruit in my_fruits[::-1]:
    print(fruit)

# Цикл for с индексами
my_list_1 = ['a', 'b', 'c', 'd']
for i in range(len(my_list_1)):
    print(f'Index: {i}, Element: {my_list_1[i]}')


#------------------------
"""
Преимущества использования индексов

Использование индексов в циклах позволяет не только получать доступ к каждому элементу, но и изменять элементы списка на месте. Это 
особенно полезно, когда нужно модифицировать список во время итерации.
"""
#------------------------
my_list_2 = ['a', 'b', 'c', 'd']
for i in range(len(my_list_2)):
    my_list_2[i] = my_list_2[i] * 2


# Использование функции enumerate()
my_list_enum = ["Apple", "Peach", "Banana", "PineApple", "Orange"]
for index, element in enumerate(my_list_enum):
    print(f'Index: {index}, Element: {element}')


"""
enumerate() идеально подходит для задач, где требуется одновременно
изменять элементы списка или сравнивать элементы с их индексами
"""
my_list_enum_2 = ["Apple", "Banana", "Orange", "Lime"]
for index, element in enumerate(my_list_enum_2):
    if index % 2 == 0:
        print(f'Element {element} at even index {index}')



# Цикл while
numbers = [1, 2, 3, 4, 5, 6, 7, 8, -1, 9, 10]
i = 0
while i < len(numbers) and numbers[i] != -1:
    print(numbers[i])
    i += 1

# Задача
"""
 В списке хранятся некоторые задания, их нужно 
 по одному из списка доставать, выполнять и удалять из списка
"""
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2]
while len(num_list) > 0:
    num_list = num_list.pop()
    print(num_list)