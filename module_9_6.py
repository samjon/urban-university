def all_variants(text):
    length = len(text)
    for size in range(1, length + 1):
        for start in range(length - size + 1): #внутренним циклом сначала пробегаемся по одиночным значениям
            yield text[start:start + size]

# Пример вызова функции и итерации через объект-генератор:
a = all_variants("abc")
for i in a:
    print(i)

