import os

from tg import db_users
from django.core.management.base import BaseCommand
from telebot import TeleBot, types

from tg.db_users import check_value, check_counter, check_lvl_user

bot = TeleBot(os.getenv('TG_TOKEN'), parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    text_greeting = f"Я - связующее звено с практиками высших уровней.\n\
Этих уровней три, каждый из них сопровождается введением.\n\
<b>Важно: выполнение практик - только твоя ответственность перед самим собой.</b>"
    db_users.check_and_add_user(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_first_q = types.KeyboardButton('Получить первую практику')
    item_info = types.KeyboardButton('Помощь')
    markup.add(item_first_q, item_info)
    bot.send_message(message.from_user.id, text_greeting, reply_markup=markup, parse_mode='HTML')


@bot.message_handler(content_types=['text'])
def send_random_templ(message):
    markup_back_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_back = types.KeyboardButton('Вернуться в главное меню')
    markup_back_menu.add(item_back)
    markup_main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    item_info = types.KeyboardButton('Помощь')
    item_next = types.KeyboardButton('Получить следующую практику')
    markup_main_menu.add(item_next, item_info)
    item_done = types.KeyboardButton('Выполнил практику')
    item_skip = types.KeyboardButton('Пропуск практики')

    if message.text == 'Получить первую практику':
        text = db_users.check_value(message)
        markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup_1.add(item_done, item_skip, item_back)
        bot.send_message(message.from_user.id, text=text, reply_markup=markup_1)

    elif message.text == 'Получить следующую практику':
        text = db_users.check_value(message)
        markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup_1.add(item_done, item_skip, item_back)
        bot.send_message(message.from_user.id, text=text, reply_markup=markup_1)

    elif message.text == 'Помощь':
        text_info = 'Каждая выполненная практика приносит один балл.\n\
Набрав определенное количество баллов, ты получаешь доступ к практикам следующего уровня.\n\
Возможность перемещаться между практикам разных уровней доступна по кнопке ниже.'
        markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item_level = types.KeyboardButton('Выбрать уровень квестов')
        markup_menu.add(item_level, item_back)
        bot.send_message(message.from_user.id, text=text_info, reply_markup=markup_menu)

    elif message.text == 'Вернуться в главное меню':
        text_menu = '3,2,1...'
        bot.send_message(message.from_user.id, text=text_menu, reply_markup=markup_main_menu)

    elif message.text == 'Выбрать уровень практики':
        markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup_menu.add(item_back)
        bot.send_message(message.from_user.id, text='3,2,1...', reply_markup=markup_menu)

    elif message.text == 'Выполнил практику':
        check_counter(message)
        text = db_users.check_value(message)
        markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item_done = types.KeyboardButton('Выполнил практику')
        item_skip = types.KeyboardButton('Пропуск практики')
        markup_1.add(item_done, item_skip, item_back)
        bot.send_message(message.from_user.id, text=text, reply_markup=markup_1)

    elif message.text == 'Пропуск практики':
        text = db_users.check_value(message)
        markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item_done = types.KeyboardButton('Выполнил практику')
        item_skip = types.KeyboardButton('Пропуск практики')
        markup_1.add(item_done, item_skip, item_back)
        bot.send_message(message.from_user.id, text=text, reply_markup=markup_1)

    elif message.text == 'Выбрать уровень квестов':
        markup_menu_lvl = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_1 = types.KeyboardButton('5 уровень')
        item_2 = types.KeyboardButton('6 уровень')
        item_3 = types.KeyboardButton('7 уровень')
        markup_menu_lvl.add(item_1, item_2, item_3, item_back)
        bot.send_message(message.from_user.id, text='Выбери уровень следующего квеста', reply_markup=markup_menu_lvl)

    elif message.text == '5 уровень':
        text_1 = check_lvl_user(message, 1)
        text_2 = db_users.check_value(message)
        markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item_done = types.KeyboardButton('Выполнил практику')
        item_skip = types.KeyboardButton('Пропуск практики')
        markup_1.add(item_done, item_skip, item_back)
        bot.send_message(message.from_user.id, text=str(text_1) + str(text_2), reply_markup=markup_1)

    elif message.text == '6 уровень':
        text_1 = check_lvl_user(message, 2)
        text_2 = db_users.check_value(message)
        markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item_done = types.KeyboardButton('Выполнил практику')
        item_skip = types.KeyboardButton('Пропуск практики')
        markup_1.add(item_done, item_skip, item_back)
        bot.send_message(message.from_user.id, text=str(text_1) + str(text_2), reply_markup=markup_1)

    elif message.text == '7 уровень':
        text_1 = check_lvl_user(message, 3)
        text_2 = db_users.check_value(message)
        markup_1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        item_done = types.KeyboardButton('Выполнил практику')
        item_skip = types.KeyboardButton('Пропуск практики')
        markup_1.add(item_done, item_skip, item_back)
        bot.send_message(message.from_user.id, text=str(text_1) + str(text_2), reply_markup=markup_1)


@bot.message_handler(commands=['quest done'])
def next_quest(message):
    pass


class Command(BaseCommand):
    help = 'TelegramBot'

    def handle(self, *args, **options):
        bot.enable_save_next_step_handlers(delay=2)  # Сохранение обработчиков
        bot.load_next_step_handlers()  # Загрузка обработчиков
        bot.polling()
