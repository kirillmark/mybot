import settings
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackQueryHandler


class BotCommands:
    care = 'Уход'
    food = 'Питание'
    character = 'Описание характера'
    about_types = 'Все о породах'
    which_type = 'Какой породы кот?'
    about_bot = 'Что может этот бот?'

    def __getattr__(self, attr):
        if 'regex_' in attr:
            attr = attr.replace('regex_', '')
            return r'^' + getattr(self, attr).replace('?', r'\?') + r'$'


bc = BotCommands()

reply_keyboard = [
    [bc.care, bc.food],
    [bc.character, bc.about_types],
    [bc.which_type, bc.about_bot],
]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def greet_user(update, context):
    update.message.reply_text('Привет, я сделан для того, чтобы помогать тебе в уходе за твоим любимцем, я готов,'
                              ' задавай вопрос!😺', reply_markup=markup)


def get_care(update, context):
    update.message.reply_text('С появлением в доме кошки многое в привычном распорядке дня поменяется.'
                              ' Питомца потребуется приучить к лотку и гигиеническим процедурам,'
                              ' наладить питание и позаботиться о том, чтобы внешняя среда была для него безопасной.'
                              ' Чтобы разобраться, как ухаживать за кошкой правильно,'
                              ' следуйте простым рекомендациям специалистов.😺', reply_markup=markup)
    keyboard = [
        [
            InlineKeyboardButton("Кот у меня недавно", callback_data="Кот у меня недавно"),
            InlineKeyboardButton("Кот у меня уже давно", callback_data="Кот у меня уже давно"),
        ],
        [
            InlineKeyboardButton("Лечение", callback_data="Лечение"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Скажите, когда у вас появился котенок?😺', reply_markup=reply_markup)


def get_nutrition(update, context):
    keyboard = [
        [
            InlineKeyboardButton("0-5", callback_data="0-5"),
            InlineKeyboardButton("5-10", callback_data="5-10"),
        ],
        [
            InlineKeyboardButton("10-12", callback_data="10-12"),
            InlineKeyboardButton("12+", callback_data="12+"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text("Скажите, сколько лет вашему коту?😺", reply_markup=reply_markup)


def character_description(update, context):
    update.message.reply_text('Характер у котика можно предугатать только когда он котенок😺', reply_markup=markup)
    update.message.reply_text("Если вы с ним часто играете, не ругаете и не кричите на него, он вырастет дружелюбным😺")
    update.message.reply_text("Если ваш котенок охотится за вашими ногами, охотно играет и не сидит без дела,"
                              " то у вас будет кот-охотник😺", reply_markup=markup)
    update.message.reply_text("Если вы часто гладите котенка, и воспитывете его, то он вырастете ласковым😺")
    update.message.reply_text("Если вы плохо относитесь к котенку, ругете его и кричите,"
                              " то он вырестете злым и своенравным котом😺", reply_markup=markup)


def get_breed(update, context):
    update.message.reply_text('Для начинающих подойдут такие породы как "Сноу-шу", Британская короткошерстная",'
                              ' "Норвежская лесная", "Японский бобтейл", "Шотландская вислоухая"😺', reply_markup=markup)
    update.message.reply_text("При должном воспитанииони могут вырасти дружелюбными😺", reply_markup=markup)
    keyboard = [
        [
            InlineKeyboardButton("Да, давай", callback_data="Да, давай"),
            InlineKeyboardButton("Нет, не надо", callback_data="Нет, не надо"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Мы можем предложить вам породы по разным характеристикам😺", reply_markup=reply_markup)


def get_what_breed_of_cat(update, context):
    update.message.reply_text("Отлично, теперь отправте мне изображение с котом,"
                              " а я с помощью AI определю его породу😺", reply_markup=markup)


def get_help(update, context):
    update.message.reply_text("Я бот который помогает тебе в уходе за твоим любимцем, я подключен в размым мед сайтам,"
                              " форумам любителей котов, поэтому мои данные на 99.9% верны😺\n"
                              "Вот некоторые команды:\n"
                              "/start - запуск бота\n"
                              "/care - инфо об уходе\n"
                              "/nutrit - инфо о питании\n"
                              "/descrip - характер\n"
                              "/breed - все о породах\n"
                              "/wht_breed - определение какой породы кот", reply_markup=markup)


def buttons(update, context):
    query = update.callback_query
    query.answer()

    # query.edit_message_text(text=f"Selected option: {query.data}")
    if query.data == "Кот у меня недавно":
        query.edit_message_text(text='Выбран вариант "Кот у меня недавно"😺')
        query.edit_message_text(text='Переезд в новый дом сопряжен с отъемом от матери и сопометников.'
                                  ' Поэтому первое время котенок будет испытывать сильный стресс и вести себя беспокойно,'
                                  ' замкнуто или агрессивно.🐱')
    elif query.data == "Кот у меня уже давно":
        query.edit_message_text(text='Выбран вариант "Кот у меня уже давно"😺')
        query.edit_message_text(text='Для тех у кого кот уже давно вот несколько пунктов которые нужно соблюдать:\n'
                                  '1. правильно подобранное питание;\n'
                                  '2. выполнение гигиенических процедур;\n'
                                  '3. оборудование комфортного места отдыха;\n'
                                  '4. своевременную вакцинацию;\n'
                                  '5. оборудование комфортного туалета;\n'
                                  '6. плановые осмотры ветеринара.🐱')
    elif query.data == "Лечение":
        query.edit_message_text(text='Какие симптомы у вашего кота?🐱')
    elif query.data == "0-5":
        query.edit_message_text(text="Для котенка подойдут такие продукты как:\n"
                                     "1. Мясо. Дают в сыром, ошпаренном или отварном виде\n"
                                     "2. Печень. Максимум 2 раза в неделю\n"
                                     "3. Каши. Не рекомендуется давать манную\n"
                                     "4. Овощи. Нельзя картофель, остальные допустимо в сыром или отварном виде\n"
                                     "5. Куриные яйца. Для котят подходит лишь желток, не чаще раза в неделю\n"
                                     "6. Молочные продукты.🐱")
    elif query.data == "5-10":
        query.edit_message_text(text='Для более старших котов в меню питомцев следует добавлять мясные субпродукты,'
                                     ' рыбу (по желанию), овощи, крупы,'
                                     ' нежирную кисломолочную продукцию (если животное не отказывается ее есть)'
                                     ' и витаминно-минеральные комплексы (только по назначению ветеринарного врача).'
                                     ' Нужно выбирать качественные и свежие продукты.🐱')
    elif query.data == "10-12":
        query.edit_message_text(text="Для более старых котов предусмотрен такой корм:\n"
                                     "Нежирное мясо. Курица, индейка телятина, говядина, нежирные сорта морской рыбы.\n"
                                     "Злаки. Гречка, рис, полба, киноа, булгур.\n"
                                     "Кисломолочная продукция.\n"
                                     "Ряженка, кефир, творог до 8% жирности.🐱")
    elif query.data == "12+":
        query.edit_message_text(text='Предлагайте небольшие порции вкусной еды или перекусы, например,'
                                     ' тунца или вареной курицы.'
                                     ' Давайте несколько небольших порций в день вместо одной или двух больших порций.'
                                     ' Влажный корм предпочтительнее сухого,'
                                     ' так как в нем больше воды и кошке легче жевать и глотать.🐱')
    elif query.data == 'Да, давай':
        keyboard = [
            [
                InlineKeyboardButton("Дружелюбный", callback_data="Дружелюбный"),
                InlineKeyboardButton("Кот-охотник", callback_data="Кот-охотник"),
            ],
            [
                InlineKeyboardButton("Ласковый", callback_data="Ласковый"),
                InlineKeyboardButton("Своенравный", callback_data="Своенравный"),
            ],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text='Какую породу вы хотите?🐱', reply_markup=reply_markup)
    elif query.data == 'Нет, не надо':
        query.edit_message_text(text='Хорошо, я могу еще чем-то вам помочь?🐱')
    elif query.data == "Дружелюбный":
        update.callback_query.message.reply_text('Вы выбрали "Дружелюбный"')
        chat_id = update.effective_chat.id
        update.callback_query.send_photo(chat_id, open('images_for_friendly/Ragdoll.jpg', 'rb'))
    elif query.data == "Кот-охотник":
        update.callback_query.message.reply_text('Вы выбрали "Кот-охотник"')
    elif query.data == "Ласковый":
        update.callback_query.message.reply_text('Вы выбрали "Ласковый"')
    elif query.data == "Своенравный":
        update.callback_query.message.reply_text('Вы выбрали "Своенравный"')


def main():

    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.regex(bc.regex_care), get_care))
    dp.add_handler(MessageHandler(Filters.regex(bc.regex_food), get_nutrition))
    dp.add_handler(MessageHandler(Filters.regex(bc.regex_character), character_description))
    dp.add_handler(MessageHandler(Filters.regex(bc.regex_about_types), get_breed))
    dp.add_handler(MessageHandler(Filters.regex(bc.regex_which_type), get_what_breed_of_cat))
    dp.add_handler(MessageHandler(Filters.regex(bc.regex_about_bot), get_help))
    dp.add_handler(CallbackQueryHandler(buttons))



    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
