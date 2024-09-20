first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. Генераторная сборка для вычисления разницы длин строк, если их длины не равны, используя zip
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# 2. Генераторная сборка для сравнения длин строк в одинаковых позициях, не используя zip
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))

