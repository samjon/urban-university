import requests

res = requests.get('https://yandex.ru') # Создаём переменную, в которую сохраним код состояния запрашиваемой страницы.

print(res) # Выводим код состояния.(Response [200] - Запрос прошёл успешно, и мы получили ответ.)

import matplotlib.pyplot as plt

# Данные для круговой диаграммы
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']

# Создание круговой диаграммы
plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)  # Круговая диаграмма с процентами
plt.title('Круговая диаграмма')  # Заголовок графика
plt.axis('equal')  # Сделать круговую диаграмму круглой
plt.show()  # Показать график

from PIL import Image, ImageFilter

# Открытие изображения
image_path = 'my_dog.jpg'  # Укажите путь к вашему изображению
img = Image.open(image_path)

# Изменение размера изображения
new_size = (800, 600)  # Новый размер (ширина, высота)
resized_img = img.resize(new_size)
resized_img.show()  # Показать измененное изображение

# Применение эффекта размытия
blurred_img = img.filter(ImageFilter.BLUR)
blurred_img.show()  # Показать размытое изображение

# Сохранение измененного изображения в другом формате
output_path = 'image_1.png'  # Укажите путь для сохранения
resized_img.save(output_path, format='PNG')

# Вывод информации о новом изображении
print(f'Изображение сохранено как: {output_path}')