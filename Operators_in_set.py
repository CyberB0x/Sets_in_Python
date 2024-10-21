# Работа с множествами через операторы

# Объединение (OR)
set1 = {1, 2, 3}
set2 = {4, 5, 6}
union_set = set1 | set2
print(union_set)

# Использование функции union()
set1 = {1, 2, 3}
set2 = {4, 5, 6}
union_set = set1.union(set2)
print(union_set)

# -----------------------------

# Пересечение (AND)
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6}
instersec_set = set1 & set2
print(instersec_set)

# Использование функции intersection ()
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6}
instersec_set = set1.intersection(set2)
print(instersec_set)

# -----------------------------

# Разность (DIFFERENCE)
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7}
diff_set = set1 - set2
print(diff_set)

# Использование функции difference ()
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7}
diff_set = set1.difference(set2)
print(diff_set)

# ----------------------------

# Симметрическая разность (SYMMETRIC DIFFERENCE)
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7, 8}
s_diff_set = set1.symmetric_difference(set2)
print(s_diff_set)