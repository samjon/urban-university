
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Создаём список длин строк из first_strings, где длина строки не менее 5 символов
first_result = [len(x) for x in first_strings if len(x) > 5]
print(first_result)

# 2. Создаём список пар слов одинаковой длины из first_strings и second_strings
second_result = [(s1, s2) for s1 in first_strings for s2 in second_strings if len(s1) == len(s2)]
print(second_result)

# 3. Создаём словарь, где ключ - строка, значение - её длина, для всех строк из объединённых списков
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}
print(third_result)