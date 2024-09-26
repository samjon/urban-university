from threading import Thread, Lock
import time

# Создание класса Knight
class Knight(Thread):
    print_lock = Lock()  # Создаем объект Lock для синхронизации печати

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        days = 0
        with self.print_lock:
            print(f"{self.name}, на нас напали!")

        while enemies > 0:
            time.sleep(1)  # Задержка на 1 секунду
            days += 1
            enemies -= self.power
            with self.print_lock:
                if enemies > 0:
                    print(f"{self.name} сражается {days} день(дня)..., осталось {enemies} воинов.")
                else:
                    print(f"{self.name} одержал победу спустя {days} дней(дня)!")
                    break

# Создание рыцарей
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ожидание окончания потоков
first_knight.join()
second_knight.join()

# Вывод строки об окончании сражения
print("Все битвы закончились!")

