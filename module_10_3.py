import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
        self.print_lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                self.balance += amount
                message = f"Пополнение: {amount}. Баланс: {self.balance}\n"
            with self.print_lock:
                print(message, end='')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            with self.lock:
                if amount <= self.balance:
                    self.balance -= amount
                    message = f"Снятие: {amount}. Баланс: {self.balance}\n"
                else:
                    message = (
                        f"Запрос отклонён, недостаточно средств.\n"
                        f"Запрос на: {amount}. Баланс: {self.balance}\n"
                    )
            with self.print_lock:
                print(message, end='')
            time.sleep(0.001)

bk = Bank()

th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()
th1.join()
th2.join()

with bk.print_lock:
    print(f'Итоговый баланс: {bk.balance}')






