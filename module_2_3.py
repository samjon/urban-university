# Задача "Нули ничто, отрицание недопустимо!":
# Дан список чисел [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# Нужно выписывать из этого списка только положительные числа до тех пор, пока не встретите отрицательное или не закончится список (выход за границу).
# Пункты задачи:
# Запишите исходный список в переменную my_list.
# Напишите цикл while с соответствующими задаче условиями.
# Используйте операторы прерывания/продолжения цикла в соответствии с условиями задачи.

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
item = 0

for item in my_list:
    if item > 0:
        while item > 0:
            print(item)
            break
    elif item == 0:
        continue
    else:
        break

