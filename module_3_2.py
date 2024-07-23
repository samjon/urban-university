# Задача "Рассылка писем":
# Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного и того же пользователя(администрации или службы поддержки). Тем не менее должна быть возможность сменить его в редких случаях.
# Попробуем реализовать функцию с подробной логикой.
#
# Создайте функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.
# Внутри функции реализовать следующую логику:
# Проверка на корректность e-mail отправителя и получателя.
# Проверка на отправку самому себе.
# Проверка на отправителя по умолчанию.

def send_email(message, recipient, sender = "university.help@gmail.com"):
    sender = str(sender)
    recipient = str(recipient)
    recipient_tuple = (recipient)
    sender_tuple = (sender)
    ends_tuple = (".com", ".ru", ".net")
    check_for_send = True
    if ("@" not in recipient) or ("@" not in sender):
        check_for_send = False
    elif not (recipient_tuple.endswith(ends_tuple)):
        check_for_send = False
    elif not (sender_tuple.endswith(ends_tuple)):
        check_for_send = False
    if check_for_send == False:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    if recipient == sender:
        return print(f'Нельзя отправить письмо самому себе!')
    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}')

#Пример выполняемого кода (тесты):
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
