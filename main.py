import telebot
from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

import useful_vars

markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
item1 = types.KeyboardButton("Программы 📃")
item3 = types.KeyboardButton("Перечень документов 💼")
item4 = types.KeyboardButton("Загрузить документы 📩")
item5 = types.KeyboardButton("Связь со специалистом 👨‍🏫")
item6 = types.KeyboardButton("Помощь 🆘")
item7 = types.KeyboardButton("Лагерь 🎒")
markup.add(item1, item7)
markup.add(item3, item4)
markup.add(item5)
markup.add(item6)
markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
ite1 = types.KeyboardButton("Подготовительный уровень ~ 5-11 лет")
ite3 = types.KeyboardButton("Базовый уровень ~ 12-15 лет")
ite4 = types.KeyboardButton("Продвинутый уровень ~ 14-17 лет")
ite5 = types.KeyboardButton('Отмена ❌')
markup1.add(ite1)
markup1.add(ite4)
markup1.add(ite3)
markup1.add(ite5)
markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
ited1 = types.KeyboardButton("Младше 14 лет 🧢")
ited2 = types.KeyboardButton("Старше 14 лет 🕶")
ited3 = types.KeyboardButton("Отмена ❌")
markup2.add(ited1)
markup2.add(ited2)
markup2.add(ited3)
markup_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
answer_key = types.KeyboardButton("Ответить на вопрос 👨")
markup_admin.add(answer_key)


admin = 999985425

bot = telebot.TeleBot('1475132639:AAHCT1bYLRizNvTNGylCrvjQGOlm2cDfEhc')


@bot.message_handler(commands=["start"])
def start(m):
    if m.chat.id == admin:
        bot.send_message(m.chat.id,
                     'Привет, я бот для менеджмента вопросов образовательной организации IT-Cube 36 школы Великого Новгорода. \nВоспользуйтесь клавиатурой чтобы взаимодействовать) ', reply_markup=markup_admin)
    else:
        bot.send_message(m.chat.id,
                         'Привет, я бот для менеджмента вопросов образовательной организации IT-Cube 36 школы Великого Новгорода. \nВоспользуйтесь клавиатурой чтобы взаимодействовать) ',
                         reply_markup=markup)
    return


@bot.message_handler(func=lambda message: "программ" in message.text.lower())
def program_view_level(m):
    bot.send_message(m.chat.id,
                         'Выберите уровень обучения: ', reply_markup=markup1)
    bot.register_next_step_handler(m, level_chosen)
    return


def level_chosen(m, i=0, h=None):
    if h == None :
        bot.send_message(m.chat.id, "---", reply_markup=markup)
    if "подготовительны" in m.text.lower() or h == "s":
        inline_kb1 = InlineKeyboardMarkup(row_width=2)
        if i == 0:
            inline_btn_2 = InlineKeyboardButton("➡", callback_data=">s" + str(i))
            inline_kb1.add(inline_btn_2)
        elif i == 3:
            inline_btn_1 = InlineKeyboardButton("⬅", callback_data="<s" + str(i))
            inline_kb1.add(inline_btn_1)
        else:
            inline_btn_1 = InlineKeyboardButton("⬅", callback_data="<s" + str(i))
            inline_btn_2 = InlineKeyboardButton("➡", callback_data=">s" + str(i))
            inline_kb1.add(inline_btn_1, inline_btn_2)
        inline_btn_3 = InlineKeyboardButton("Поступить ✅", callback_data="*")
        inline_kb1.add(inline_btn_3)
        bot.send_message(m.chat.id, "*" + useful_vars.programs_start[i][0] + "*" + "\n\n" + useful_vars.programs_start[i][1], parse_mode="Markdown", reply_markup=inline_kb1)
        return

    elif 'базовы' in m.text.lower() or h == "b":
        inline_kb1 = InlineKeyboardMarkup(row_width=2)
        if i == 0:
            inline_btn_2 = InlineKeyboardButton("➡", callback_data=">b" + str(i))
            inline_kb1.add(inline_btn_2)
        elif i == 11:
            inline_btn_1 = InlineKeyboardButton("⬅", callback_data="<b" + str(i))
            inline_kb1.add(inline_btn_1)
        else:
            inline_btn_1 = InlineKeyboardButton("⬅", callback_data="<b" + str(i))
            inline_btn_2 = InlineKeyboardButton("➡", callback_data=">b" + str(i))
            inline_kb1.add(inline_btn_1, inline_btn_2)
        inline_btn_3 = InlineKeyboardButton("Поступить ✅", callback_data="*")
        inline_kb1.add(inline_btn_3)
        bot.send_message(m.chat.id,
                         "*" + useful_vars.programs_base[i][0] + "*" + "\n\n" + useful_vars.programs_base[i][1],
                         parse_mode="Markdown", reply_markup=inline_kb1)
        return

    elif "продвинуты" in m.text.lower() or h == "a":
        inline_kb1 = InlineKeyboardMarkup(row_width=2)
        if i == 0:
            inline_btn_2 = InlineKeyboardButton("➡", callback_data=">a" + str(i))
            inline_kb1.add(inline_btn_2)
        elif i == 3:
            inline_btn_1 = InlineKeyboardButton("⬅", callback_data="<a" + str(i))
            inline_kb1.add(inline_btn_1)
        else:
            inline_btn_1 = InlineKeyboardButton("⬅", callback_data="<a" + str(i))
            inline_btn_2 = InlineKeyboardButton("➡", callback_data=">a" + str(i))
            inline_kb1.add(inline_btn_1, inline_btn_2)
        inline_btn_3 = InlineKeyboardButton("Поступить ✅", callback_data="*")
        inline_kb1.add(inline_btn_3)
        bot.send_message(m.chat.id,
                         "*" + useful_vars.programs_adv[i][0] + "*" + "\n\n" + useful_vars.programs_adv[i][1],
                         parse_mode="Markdown", reply_markup=inline_kb1)
        return
    elif "отмен" in m.text.lower():
        bot.send_message(m.chat.id, "Отменено ❌", reply_markup=markup)
        return
    else:
        bot.send_message(m.chat.id, "Извините, я вас не понял, попробуйте снова...", reply_markup=markup1)
        bot.register_next_step_handler(m, level_chosen)
        return


@bot.message_handler(func=lambda message: "перечен" in message.text.lower())
def doc_choose(m):
    bot.send_message(m.chat.id,
                         'Выберите возраст ребенка:', reply_markup=markup2)
    bot.register_next_step_handler(m, age_choosen)
    return


def age_choosen(m):
    if "старш" in m.text.lower():
        file = open("Soglasie_na_obrabotku_dannyh_nesovershennoletnego_starshe_14_let.docx", "rb")
        file2 = open("Zayavlenie_na_postuplenie.pdf", "rb")
        bot.send_message(m.chat.id, 'Документы для поступления - согласие на обработку персональных данных (старше 14 лет) и заявление на поступление. \n\nПосле заполнения можете загрузить их в разделе "Загрузить документы". ', reply_markup=markup)
        bot.send_document(m.chat.id, file)
        bot.send_document(m.chat.id, file2)
        return
    elif "младш" in m.text.lower():
        file = open("Soglasie_na_obrabotku_ot_dannyh_zakonnogo_predstavitelya_(mladshe_14).docx", "rb")
        file2 = open("Zayavlenie_na_postuplenie.pdf", 'rb')
        bot.send_message(m.chat.id,
                         'Документы для поступления - согласие на обработку персональных данных (младше 14 лет) и заявление на поступление. \n\nПосле заполнения можете загрузить их в разделе "Загрузить документы". ', reply_markup=markup)
        bot.send_document(m.chat.id, file)
        bot.send_document(m.chat.id, file2)
        return
    elif "отмен" in m.text.lower():
        bot.send_message(m.chat.id, "Отменено ❌", reply_markup=markup)
        return
    else:
        bot.send_message(m.chat.id, "Извините, я вас не понимаю, попробуйте снова...")
        bot.register_next_step_handler(m, age_choosen)
        return


@bot.callback_query_handler(func=None)
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    if callback_query.data == "*":
        doc_choose(callback_query.message)
        return
    i = int(callback_query.data[-1])
    if callback_query.data[-3] == ">":
        i += 1
    elif callback_query.data[-3] == "<":
        i -= 1
    level_chosen(callback_query.message, i, callback_query.data[-2])
    return



@bot.message_handler(func=lambda message: "загрузит" in message.text.lower())
def send_doc(m):

    bot.send_message(m.chat.id,
                         'Вы можете отправить документы к нам на почту! \n*itcube@3653.ru*', parse_mode="Markdown")
    return



@bot.message_handler(func=lambda message: "связь" in message.text.lower())
def send_doc(m):
    fin = open("users_questions.txt", "r")
    if str(m.chat.id) in fin.read():
        bot.send_message(m.chat.id, "Вы уже задали вопрос техподдержке, дождитесь пожалуйста ответа...")
        return
    bot.send_message(m.chat.id,
                         'Введите пожалуйста сообщение для техподдержки', reply_markup=markup)
    bot.register_next_step_handler(m, to_spec)
    return


def to_spec(m):
    fin = open("users_questions.txt", "r")
    if str(m.chat.id) not in fin.read():
        bot.send_message(m.chat.id, "Спасибо, скоро вам поступит ответ от специалистов!")
        new_user = str(m.chat.id)+"\n"
        fin = open("users_questions.txt", "a")
        fin.write(new_user)
        fin.close()
        bot.send_message(admin, "*Вопрос №"+str(m.chat.id)+":* " + m.text, parse_mode="Markdown")
        return


@bot.message_handler(func=lambda message: "ответит" in message.text.lower())
def answer_spec(m):
    if m.chat.id != admin:
        we_dont_know(m)
        return
    else:
        markup_answer = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_answer.add(types.KeyboardButton("Отмена ❌"))
        fin = open("users_questions.txt", "r")
        if fin.read() == "":
            bot.send_message(m.chat.id, "Извините, вопросов пока нет...")
            return
        fin = open("users_questions.txt", "r")
        lines = fin.read().split("\n")
        for i in lines:
            if i != "":
                item = types.KeyboardButton(str(i))
                markup_answer.add(item)
        fin.close()
        bot.send_message(m.chat.id, "Выберите номер вопроса:", reply_markup=markup_answer)
        bot.register_next_step_handler(m, send_answer)
        return
user_toansw = 0


def send_answer(m):
    if "отмена" in m.text.lower():
        bot.send_message(m.chat.id, "Отменено ❌", reply_markup=markup_admin)
        return
    global user_toansw
    user_toansw = m.text
    fin = open("users_questions.txt", "r")
    lines = fin.read().split("\n")
    if user_toansw not in lines:
        bot.send_message(m.chat.id, "Извините, но такого вопроса нет или на него уже ответили, попробуйте снова...")
        bot.register_next_step_handler(m, send_answer)
        fin.close()
        return
    bot.send_message(m.chat.id, "Введите ответ: ")
    bot.register_next_step_handler(m, send_answer2)
    return


def send_answer2(m):
    global user_toansw
    user = user_toansw
    bot.send_message(m.chat.id, "Вы ответили на вопрос №" + user, reply_markup=markup_admin)
    fin = open("users_questions.txt", "r")
    old_file = fin.read()
    new_file = old_file.replace(user + "\n", "")
    fin = open("users_questions.txt", "w")
    fin.write(new_file)
    fin.close()
    bot.send_message(user, "Ответ специалиста на ваш вопрос: " + m.text)
    return


@bot.message_handler(func=lambda message: "помощ" in message.text.lower())
def help(m):
    bot.send_message(m.chat.id,
                     'В разработке...')
    return


@bot.message_handler(func=lambda message: "лагер" in message.text.lower())
def camp(m):
    bot.send_message(m.chat.id,
                     'Ознакомьтесь с информацией по ссылке - *https://3653.ru/detozdlag/*', parse_mode="Markdown")
    return


@bot.message_handler(func=None)
def we_dont_know(m):
    bot.send_message(m.chat.id,
                         'Извините, я вас не понимаю')
    return


bot.polling(none_stop=True, interval=0)
