import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
import asyncio
from crud_functions import *

API_TOKEN = '8187944597:AAE1fXVzEvBdScxsKILL2-jTtvLaMDmZVxQ'  # Замените на ваш токен

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание объекта бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Определение состояний
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()
    buying_list_shown = State()  # Добавляем состояние для отслеживания вывода списка продуктов

# Создание клавиатуры с кнопками
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать')],
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')],
        [KeyboardButton(text='Регистрация')]  # Добавляем кнопку "Регистрация"
    ],
    resize_keyboard=True
)


# Создание Inline клавиатуры для выбора опций расчета калорий
def inline_calories_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')],
            [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')]
        ]
    )

# Создание Inline клавиатуры для продуктов
def inline_product_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Product1', callback_data='product_buying')],
            [InlineKeyboardButton(text='Product2', callback_data='product_buying')],
            [InlineKeyboardButton(text='Product3', callback_data='product_buying')],
            [InlineKeyboardButton(text='Product4', callback_data='product_buying')]
        ]
    )

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью. Выберите действие:", reply_markup=keyboard)


@dp.message(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=inline_calories_keyboard())

@dp.callback_query(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Формула Миффлина-Сан Жеора:\n"
                              "Для женщин: 10 * вес + 6.25 * рост - 5 * возраст + 5\n"
                              "Для мужчин: 10 * вес + 6.25 * рост - 5 * возраст + 5")
    await call.answer()

@dp.callback_query(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserState.age)
    await call.message.answer('Введите свой возраст:')
    await call.answer()

@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await state.set_state(UserState.growth)
    await message.answer('Введите свой рост (в см):')

@dp.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await state.set_state(UserState.weight)
    await message.answer('Введите свой вес (в кг):')

@dp.message(UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)

    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f'Ваша норма калорий: {calories:.2f} ккал.')

    await state.clear()

@dp.message(lambda message: message.text == 'Информация')
async def info_handler(message: types.Message):
    await message.answer("Этот бот поможет вам рассчитать норму калорий на основе ваших параметров.")

@dp.message(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message, state: FSMContext):
    # Проверяем, был ли уже показан список продуктов
    if await state.get_state() == UserState.buying_list_shown:
        await message.answer("Список продуктов уже показан. Выберите продукт.")
        return

    products = get_all_products()  # Получаем все продукты из базы данных

    for product in products:
        title, description, price = product
        await message.answer(
            f'Название: {title} | Описание: {description} | Цена: {price}₽'
        )

        # Использование FSInputFile для отправки изображения (если нужно)
        image_path = f"{title.lower().replace(' ', '_')}.jpg"  # Предполагается, что изображения имеют соответствующие названия
        if os.path.exists(image_path):  # Проверяем, существует ли файл
            await message.answer_photo(photo=FSInputFile(image_path))
        else:
            await message.answer("Изображение недоступно.")

    await message.answer('Выберите продукт для покупки:', reply_markup=inline_product_keyboard())

    # Устанавливаем состояние, что список продуктов уже показан
    await state.set_state(UserState.buying_list_shown)

@dp.callback_query(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery, state: FSMContext):
    logging.info(f"User {call.from_user.id} clicked 'product_buying'")
    await call.answer()
    await call.message.answer("Вы успешно приобрели продукт!", reply_markup=types.ReplyKeyboardRemove())  # Убираем клавиатуру

    # Очищаем состояние, чтобы список продуктов можно было показать снова
    await state.clear()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


@dp.message(lambda message: message.text == 'Регистрация')
async def sing_up(message: types.Message, state: FSMContext):
    await message.answer("Введите имя пользователя (только латинский алфавит):")
    await state.set_state(RegistrationState.username)  # Используем метод set_state


@dp.message(RegistrationState.username)
async def set_username(message: types.Message, state: FSMContext):
    username = message.text
    if not username.isalpha():
        await message.answer("Имя пользователя должно содержать только латинские буквы. Попробуйте снова.")
        return

    if is_included(username):
        await message.answer("Пользователь существует, введите другое имя:")
        return

    await state.update_data(username=username)
    await message.answer("Введите свой email:")
    await state.set_state(RegistrationState.email)  # Используем метод set_state


@dp.message(RegistrationState.email)
async def set_email(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer("Введите свой возраст:")
    await state.set_state(RegistrationState.age)  # Используем метод set_state


@dp.message(RegistrationState.age)
async def set_age(message: types.Message, state: FSMContext):
    age = message.text
    if not age.isdigit() or int(age) <= 0:
        await message.answer("Возраст должен быть положительным числом. Попробуйте снова.")
        return

    data = await state.get_data()

    add_user(data['username'], data['email'], int(age))

    await message.answer("Регистрация завершена! Добро пожаловать!")

    await state.clear()  # Используем clear() вместо finish()


# Обработчик для всех остальных сообщений
@dp.message()
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')

async def main():
    # Инициализация базы данных и добавление тестовых данных (если необходимо)
    initiate_db()
    #add_sample_products()

    # Запускаем бота
    await dp.start_polling(bot)


async def main():
    initiate_db()
    add_sample_products()  # Если нужно добавить тестовые данные

    # Запускаем бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
