
# Практическое задание по уроку "Базовые структуры данных"
# Задача 1 (просто) "Арифметика":
# Напишите в начале программы однострочный комментарий: "1st program".
# Выведите на экран(в консоль) результат: возведение числа 9 в степень 0.5, после умножение на 5.
# Предполагаемый результат: 15.0

# "1st program"
print(9 ** 0.5 * 5)

# Задача 2 (просто) "Сравнение, or, and":
# Напишите в начале программы однострочный комментарий: "2nd program".
# Убедитесь в том что 9.99 больше 9.98 и 1000 не равно 1000.1 одновременно, выведете результат на экран(в консоль)
#  Предполагаемый результат: True

# "2nd program"
print(9.99 > 9.98 and 1000 != 1000.1)

# Задача 3 (средне) "Сложная арифметика":
# Напишите в начале программы однострочный комментарий: "3rd program".
# Дано два целых четырёхзначных числа: 1234 и 5678.
# Выведите на экран(в консоль) сумму серединных чисел исходных данных (23 и 67).
# Предполагаемый результат: 90

# "3rd program"
print((1234 % 1000 // 10) + (5678 % 1000 // 10))

# Задача 4 (сложно) "Всё, везде и сразу":
# Напишите в начале программы однострочный комментарий: "4th program".
# Дано два дробных числа: 13.42 и 42.13.
# Необходимо убедиться в том, что целая часть хотя бы одного из чисел равна дробной части другого. Например: 13 == 13 (13.42, 42.13) или 42 == 42 (13.42, 42.13).
# Предполагаемые результат: True

# "4th program"
print((int(13.42) == int((42.13 - int(42.13)) * 100)) or (int(42.13) == int((13.42 - int(13.42)) * 100)))
