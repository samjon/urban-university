def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        func_name = func.__name__
        results[func_name] = func(int_list)
    return results

# Пример выполнения функции
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

