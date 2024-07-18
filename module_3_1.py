# Задача "Счётчик вызовов":
# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция. К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
# Давайте реализуем данную фишку самостоятельно!
#
# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
# Пункты задачи:
# Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).

calls = 0
def count_calls() -> int:
    global calls
    calls += 1                                              # меняем значение глобальной переменной
    return calls
def string_info(string):
    count_calls()                                           # вызываем счётчик
    line_length = len(string)                               # находим длину строки
    apper_line = string.upper()                             # создаём новую строку в верхнем регистре
    lower_line = string.lower()                             # создаём новую строку в нижнем регистре
    string_tuple = (line_length, apper_line, lower_line)    # создаём кортеж
    return string_tuple                                     # возвращаем кортеж
def is_contains(string, list_to_search):
    count_calls()                                           # вызываем счётчик
    string = string.upper()                                 # приводим строку к верхнему регистру
    line1 = ' '.join(list_to_search)                        # из списка делаем строку с разделителем ввиде пробела
    line1 = line1.upper()                                   # приводим новую строку к верхнему регистру

    if string in line1:                                     # цикл на проверку содержится ли искомая строка в новой
        return True
    else:
        return False

print(string_info("1234567890ABCabcABCabcABCabc"))
print(string_info("ABCabcABCabcABCabc"))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)