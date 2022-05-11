import telebot


bot = telebot.TeleBot('5354654063:AAFJsCbnLDJfsF1nXTQc9j1axshkTU3PLac')


@bot.message_handler(commands=["start"])
def start(m):
    bot.send_message(m.chat.id,
                     'Привет, я бот c Великого Новгорода, пришел дабы проблемы твои решить, учительские да ученические. А ежели чего не понятно /help снизу писывай!')
    return


@bot.message_handler(commands=["help"])
def get_text_messages(m):
    bot.send_message(m.chat.id,
                     'А чего непонятного то тебе? Привет да пока сказывай, и будет тебе счастие!')
    return


@bot.message_handler(func=lambda message: "привет" in message.text.lower())
def hi(m):
    bot.send_message(m.chat.id,
                         'И тебе привет, сударь заморский!')
    return


@bot.message_handler(func=lambda message: "пока" in message.text.lower())
def hi_2(m):
    bot.send_message(m.chat.id,
                         'А куда это мы собралися?')
    return



@bot.message_handler(func=None)
def we_dont_know(m):
    bot.send_message(m.chat.id,
                         'Говаривай-ка ты на кириллице доброй!')
    return


bot.polling(none_stop=True, interval=0)
