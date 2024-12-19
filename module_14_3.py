import logging
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
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
        [KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')]  # Добавляем кнопку "Купить"
    ],
    resize_keyboard=True
)

# Создание Inline клавиатуры для продуктов
def inline_product_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Omega-3', callback_data='product_buying')],
            [InlineKeyboardButton(text='Vitamin C', callback_data='product_buying')],
            [InlineKeyboardButton(text='B-complex', callback_data='product_buying')],
            [InlineKeyboardButton(text='Hyaluronic acid', callback_data='product_buying')]
        ]
    )

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        'Привет! Я бот, помогающий твоему здоровью. Выберите действие:',
        reply_markup=keyboard
    )

@dp.message(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    await message.answer('Выберите опцию:', reply_markup=inline_keyboard)

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
async def get_buying_list(message: types.Message):
    products = [
        {"name": "Omega-3", "description": "fish oil", "price": 100, "image": "image1.jpg"},
        {"name": "Vitamin C", "description": "Витамин С", "price": 200, "image": "image2.jpg"},
        {"name": "B-complex", "description": "B-комплекс", "price": 300, "image": "image3.jpg"},
        {"name": "Hyaluronic acid", "description": "Гиалуроновая кислота", "price": 400, "image": "image4.jpg"}
    ]

    for product in products:
        await message.answer(
            f'Название: {product["name"]} | Описание: {product["description"]} | Цена: {product["price"]}₽'
        )

        # Использование FSInputFile для отправки изображения
        image_path = product["image"]
        await message.answer_photo(photo=FSInputFile(image_path))

    await message.answer('Выберите продукт для покупки:', reply_markup=inline_product_keyboard())

@dp.callback_query(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer("Вы успешно приобрели продукт!")

# Обработчик для всех остальных сообщений
@dp.message()
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')

async def main():
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
