def introspection_info(obj):
    # Получение типа объекта
    obj_type = type(obj).__name__

    # Получение атрибутов объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    # Получение методов объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    # Получение модуля, к которому принадлежит объект
    module = getattr(obj, '__module__', None)  # Используем getattr для безопасного доступа

    # Создание словаря с информацией об объекте
    info = {
        'type': obj_type,
        'attributes': attributes,
        'methods': methods,
        'module': module,
    }

    return info


# Пример использования функции
number_info = introspection_info(42)
print(number_info)

string_info = introspection_info("Hello, World!")
print(string_info)

list_info = introspection_info([1, 2, 3])
print(list_info)