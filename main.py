import telebot
from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

import useful_vars
cancel_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
cancel_markup.add(types.KeyboardButton("Отмена ❌"))
markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
item1 = types.KeyboardButton("Программы 📃")
item3 = types.KeyboardButton("Перечень документов 💼")
item5 = types.KeyboardButton("Cвязь с администрацией 👨‍🏫")
item6 = types.KeyboardButton("Ответы на частые вопросы 🆘")
item7 = types.KeyboardButton("Мы в соцсетях📲")
item8 = types.KeyboardButton("Оставить отзыв о работе нашего бота📝")
markup.add(item1, item3)
markup.add(item5, item6)
markup.add(item7, item8)
markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
ited1 = types.KeyboardButton("До 14 лет 🧢")
ited2 = types.KeyboardButton("От 14 лет 🕶")
ited3 = types.KeyboardButton("Отмена ❌")
markup2.add(ited1)
markup2.add(ited2)
markup2.add(ited3)
markup_admin = types.ReplyKeyboardMarkup(resize_keyboard=True)
answer_key = types.KeyboardButton("Ответить на вопрос 👨")
markup_admin.add(answer_key)
markup_directions = types.ReplyKeyboardMarkup(resize_keyboard=True)


admin = 1269837862

def to_int(var):
    try:
        int(var)
    except Exception:
        return False
    return True

bot = telebot.TeleBot('5354654063:AAFJsCbnLDJfsF1nXTQc9j1axshkTU3PLac')


@bot.message_handler(commands=["start"])
def start(m):
    if m.chat.id == admin:
        bot.send_message(m.chat.id,
                     'Привет, я бот для менеджмента вопросов образовательной организации IT-Cube 36 школы Великого Новгорода. \nВоспользуйтесь клавиатурой чтобы взаимодействовать))) ', reply_markup=markup_admin)
    else:
        bot.send_message(m.chat.id,
                         'Привет, я бот для менеджмента вопросов образовательной организации IT-Cube 36 школы Великого Новгорода. \nВоспользуйтесь клавиатурой чтобы взаимодействовать))) ',
                         reply_markup=markup)
    return


@bot.message_handler(func=lambda message: "программ" in message.text.lower())
def program_view_level(m):
    bot.send_message(m.chat.id,
                         'Введите возраст, только цифры(!): ', reply_markup=cancel_markup)
    bot.register_next_step_handler(m, age_chosen)
    return


s = 0


def age_chosen(m):
    global s
    global markup_directions
    if "отмена" in m.text.lower():
        bot.send_message(m.chat.id, "Отменено!", reply_markup=markup)
        return
    elif to_int(m.text):
        s = int(m.text)
    else:
        bot.send_message(m.chat.id,
                         "Извините, я вас не понял, попробуйте снова...")
        bot.register_next_step_handler(m, age_chosen)
        return
    not_enough_old = True


    markup_directions = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in useful_vars.game_dev:
        if s in i[1]:
            markup_directions.add(types.KeyboardButton(i[0]))
            not_enough_old = False

    for i in useful_vars.prog_mains:
        if s in i[1]:
            markup_directions.add(types.KeyboardButton(i[0]))
            not_enough_old = False

    for i in useful_vars.practical_prog:
        if s in i[1]:
            markup_directions.add(types.KeyboardButton(i[0]))
            not_enough_old = False

    for i in useful_vars.media:
        if s in i[1]:
            markup_directions.add(types.KeyboardButton(i[0]))
            not_enough_old = False


    for i in useful_vars.tech_construct:
        if s in i[1]:
            markup_directions.add(types.KeyboardButton(i[0]))
            not_enough_old = False


    for i in useful_vars.it_safety:
        if s in i[1]:
            markup_directions.add(types.KeyboardButton(i[0]))
            not_enough_old = False

    markup_directions.add(types.KeyboardButton("Назад ⬅"))
    markup_directions.add(types.KeyboardButton('Отмена ❌'))
    if not_enough_old == False:
        bot.send_message(m.chat.id, "Доступные для вас курсы:", reply_markup=markup_directions)
        bot.register_next_step_handler(m, show_fac)
    else:
        bot.send_message(m.chat.id, "Извините, у нас нет курсов для вашего возраста...", reply_markup=markup)
    return


def show_fac(m):
    send_something = False
    markup_direction = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_direction.add(types.KeyboardButton("Назад⬅"), types.KeyboardButton("Поступить✅"))
    if "назад" in m.text.lower():
        bot.send_message(m.chat.id, "Введите возраст, только цифры(!): ", reply_markup=cancel_markup)
        bot.register_next_step_handler(m, age_chosen)
        return
    elif "отмена" in m.text.lower():
        bot.send_message(m.chat.id, "Отменено!", reply_markup=markup)
        return
    for i in useful_vars.game_dev:
        if i[0].lower() == m.text.lower():
            send_something = True
            if len(i) == 3:
                bot.send_message(m.chat.id,
                                  "*" + i[0] + "*\n" + "(" + str(i[1][0]) + "-" + str(i[1][-1]) + ")" + "\n" + i[2],
                                    parse_mode="Markdown", reply_markup=markup_direction)
            else:
                bot.send_message(m.chat.id, "*" + i[0] + "*\n" + "(" + str(i[1][0]) + "-" + str(i[1][-1]) + ")",
                                     parse_mode="Markdown", reply_markup=markup_direction)
            bot.register_next_step_handler(m, contin)

    for i in useful_vars.prog_mains:
        if i[0].lower() == m.text.lower():
            send_something = True
            if len(i) == 3:
                bot.send_message(m.chat.id,
                                     "*" + i[0] + "*\n" + "(" + str(i[1][0]) + "-" + str(i[1][-1]) + ")" + "\n" + i[2],
                                     parse_mode="Markdown", reply_markup=markup_direction)
            else:
                bot.send_message(m.chat.id,
                                     "*" + i[0] + "*\n" + "(" + str(i[1][0]) + "-" + str(i[1][-1]) + ")",
                                     parse_mode="Markdown", reply_markup=markup_direction)
            bot.register_next_step_handler(m, contin)
    for i in useful_vars.practical_prog:
        if i[0].lower() == m.text.lower():
            send_something = True
            if len(i) == 3:
                bot.send_message(m.chat.id,
                                     "*" + i[0] + "*\n" + "(" + str(i[1][0]) + "-" + str(i[1][-1]) + ")" + "\n" + i[2],
                                     parse_mode="Markdown", reply_markup=markup_direction)
            else:
                bot.send_message(m.chat.id,
                                     "*" + i[0] + "*\n" + "(" + str(i[1][0]) + "-" + str(i[1][-1]) + ")",
                                     parse_mode="Markdown", reply_markup=markup_direction)
            bot.register_next_step_handler(m, contin)
    for i in useful_vars.tech_construct:
        if i[0].lower() == m.text.lower():
            send_something = True
            if len(i) == 3:
                bot.send_message(m.chat.id,
                                     "*" + i[0] + "*\n" + "(" + str(i[1][0]) + "-" + str(i[1][-1]) + ")" + "\n" + i[2],
                                     parse_mode="Markdown", reply_markup=markup_direction)
            else:
                bot.send_message(m.chat.id,
                                     "*" + i[0] + "*\n" + "(" + str(i[1][0]) + "-" + str(i[1][-1]) + ")",
                                     parse_mode="Markdown", reply_markup=markup_direction)
            bot.register_next_step_handler(m, contin)
    for i in useful_vars.it_safety:
        if i[0].lower() == m.text.lower():
            send_something = True
            if len(i) == 3:
                bot.send_message(m.chat.id,
                                    "*" + i[0] + "*\n" + "(" + str(i[1][0]) + "-" + str(i[1][-1]) + ")" + "\n" + i[2],
                                     parse_mode="Markdown", reply_markup=markup_direction)
            else:
                bot.send_message(m.chat.id,
                                     "*" + i[0] + "*\n" + "(" + str(i[1][0]) + "-" + str(i[1][-1]) + ")",
                                     parse_mode="Markdown", reply_markup=markup_direction)
            bot.register_next_step_handler(m, contin)

    for i in useful_vars.media:
        if i[0].lower() == m.text.lower():
            send_something = True
            if len(i) == 3:
                bot.send_message(m.chat.id,
                                     "*" + i[0] + "*\n" + "(" + str(i[1][0]) + "-" + str(i[1][-1]) + ")" + "\n" + i[2],
                                     parse_mode="Markdown", reply_markup=markup_direction)
            else:
                bot.send_message(m.chat.id,
                                     "*" + i[0] + "*\n" + "\n" + "(" + str(i[1][0]) + "-" + str(i[1][-1]) + ")",
                                     parse_mode="Markdown", reply_markup=markup_direction)
            bot.register_next_step_handler(m, contin)
    if not send_something:
        bot.send_message(m.chat.id,
                         "Извините, я вас не понял, попробуйте снова...")
        bot.register_next_step_handler(m, show_fac)
    return


def contin(m):
    markup_direction = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_direction.add(types.KeyboardButton("Назад⬅"), types.KeyboardButton("Поступить✅"))
    if "поступит" in m.text.lower():
        doc_choose(m)
        return
    elif "назад" in m.text.lower():
        bot.send_message(m.chat.id, "Назад◀", reply_markup=markup_directions)
        bot.register_next_step_handler(m, show_fac)
        return
    else:
        bot.send_message(m.chat.id,
                         "Извините, я вас не понял...", reply_markup=markup_direction)
        bot.register_next_step_handler(m, contin)
        return


@bot.message_handler(func=lambda message: "перечен" in message.text.lower())
def doc_choose(m):
    bot.send_message(m.chat.id,
                         'Выберите возраст ребенка:', reply_markup=markup2)
    bot.register_next_step_handler(m, age_choosen2)
    return


def age_choosen2(m):
    if "отмен" in m.text.lower():
        bot.send_message(m.chat.id, "Отменено ❌", reply_markup=markup)
        return
    elif "от" in m.text.lower():
        file = open("Soglasie_na_obrabotku_dannyh_nesovershennoletnego_starshe_14_let.docx", "rb")
        file2 = open("Zayv.pdf", "rb")
        bot.send_message(m.chat.id, 'Документы для поступления - согласие на обработку персональных данных (старше 14 лет) и заявление на поступление. \n\nПосле заполнения их можно оставить на вахте МАОУ "Школа №36" или в отсканированном виде отправить по почте itcube@3653.ru ', reply_markup=markup)
        bot.send_document(m.chat.id, file)
        bot.send_document(m.chat.id, file2)
        return
    elif "до" in m.text.lower():
        file = open("Soglasie_na_obrabotku_ot_dannyh_zakonnogo_predstavitelya_(mladshe_14).docx", "rb")
        file2 = open("Zayv.pdf", 'rb')
        bot.send_message(m.chat.id,
                         'Документы для поступления - согласие на обработку персональных данных (младше 14 лет) и заявление на поступление. \n\nПосле заполнения их можно оставить на вахте МАОУ "Школа №36" или в отсканированном виде отправить по почте itcube@3653.ru', reply_markup=markup)
        bot.send_document(m.chat.id, file)
        bot.send_document(m.chat.id, file2)
        return
    else:
        bot.send_message(m.chat.id, "Извините, я вас не понимаю, попробуйте снова...")
        bot.register_next_step_handler(m, age_choosen2)
        return


@bot.callback_query_handler(func=None)
def process_callback_button1(callback_query: types.CallbackQuery):
    bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
    i = int(callback_query.data[-1])
    if callback_query.data[-2] == ">":
        i += 1
    elif callback_query.data[-2] == "<":
        i -= 1
    help(callback_query.message, i)
    return


@bot.message_handler(func=lambda message: "администра" in message.text.lower())
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


user_toansw = ""


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
    bot.send_message(user, "*Ответ специалиста на ваш вопрос:* " + m.text, parse_mode="Markdown")
    return


@bot.message_handler(func=lambda message: "ответы на " in message.text.lower())
def help(m, i=0):
    inline_kb1 = InlineKeyboardMarkup(row_width=2)
    if i == 0:
        inline_btn_2 = InlineKeyboardButton("➡", callback_data=">" + str(i))
        inline_kb1.add(inline_btn_2)
    elif i == len(useful_vars.faq) - 1:
        inline_btn_1 = InlineKeyboardButton("⬅", callback_data="<" + str(i))
        inline_kb1.add(inline_btn_1)
    else:
        inline_btn_1 = InlineKeyboardButton("⬅", callback_data="<" + str(i))
        inline_btn_2 = InlineKeyboardButton("➡", callback_data=">" + str(i))
        inline_kb1.add(inline_btn_1, inline_btn_2)
    bot.send_message(m.chat.id,
                     "⭕*Ответы на часто задаваемые вопросы*⭕\n\n🔴*Вопрос:* " + useful_vars.faq[i][0] + "\n\n🔵*Ответ:* " + useful_vars.faq[i][1], parse_mode="Markdown", reply_markup=inline_kb1)
    return


@bot.message_handler(func=lambda message: "кванториум" in message.text.lower())
def camp(m):
    bot.send_message(m.chat.id,
                     'Мы такое не любим...', parse_mode="Markdown")
    return


@bot.message_handler(func=lambda message: "соцсет" in message.text.lower())
def site_vk(m):
    bot.send_message(m.chat.id,
                     '*Наш ВК* - https://vk.com/itcubevn', parse_mode="Markdown")
    bot.send_message(m.chat.id,
                     '*Наш сайт* - https://itcube-vn.ru/',
                     parse_mode="Markdown")
    return


@bot.message_handler(func=lambda message: "отзыв" in message.text.lower())
def site_vk(m):
    bot.send_message(m.chat.id,
                     'Введите ваш отзыв: ', parse_mode="Markdown")
    bot.register_next_step_handler(m, bot_send_feedback)
    return


def bot_send_feedback(m):
    bot.send_message(m.chat.id,
                     'Спасибо, нам это важно!', parse_mode="Markdown")
    bot.send_message(999985425, m.text)
    return


@bot.message_handler(func=None)
def we_dont_know(m):
    bot.send_message(m.chat.id,
                         'Извините, я вас не понимаю(((\nПопробуйте команду /start...')
    return

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        bot.send_message(999985425, str(e))
        print(str(e))