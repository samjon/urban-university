import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

API_TOKEN = 'BOT_TOKEN'  # Замените на ваш токен

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

# Создание клавиатуры с кнопками
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать')],
        [KeyboardButton(text='Информация')]
    ],
    resize_keyboard=True
)

# Создание Inline клавиатуры с кнопками
inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')],
        [InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')]
    ]
)

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        'Привет! Я бот, помогающий твоему здоровью. Выберите действие:',
        reply_markup=keyboard  # Используем обычную клавиатуру в ответе
    )

@dp.message(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)  # Отправляем Inline клавиатуру

@dp.callback_query(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Формула Миффлина-Сан Жеора:\n"
                              "Для женщин: 10 * вес + 6.25 * рост - 5 * возраст + 5\n"
                              "Для мужчин: 10 * вес + 6.25 * рост - 5 * возраст + 5")
    await call.answer()  # Подтверждаем обработку callback

@dp.callback_query(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await state.set_state(UserState.age)  # Устанавливаем состояние age
    await call.message.answer('Введите свой возраст:')
    await call.answer()  # Подтверждаем обработку callback

@dp.message(UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)  # Сохраняем возраст
    await state.set_state(UserState.growth)  # Переходим к состоянию growth
    await message.answer('Введите свой рост (в см):')

@dp.message(UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)  # Сохраняем рост
    await state.set_state(UserState.weight)  # Переходим к состоянию weight
    await message.answer('Введите свой вес (в кг):')

@dp.message(UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)  # Сохраняем вес

    data = await state.get_data()  # Получаем все сохраненные данные
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Формула Миффлина - Сан Жеора для женщин (можно изменить на мужскую формулу)
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f'Ваша норма калорий: {calories:.2f} ккал.')

    await state.clear()  # Завершаем состояние

@dp.message(lambda message: message.text == 'Информация')
async def info_handler(message: types.Message):
    await message.answer("Этот бот поможет вам рассчитать норму калорий на основе ваших параметров.")

async def main():
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
