from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import settings
from telegram import ReplyKeyboardMarkup


key_1 = KeyboardButton('Уход')
key_2 = KeyboardButton('Питание')
key_3 = KeyboardButton('Описание характера')
key_4 = KeyboardButton('Все о породах')
key_5 = KeyboardButton('Какой породы кот?')
key_6 = KeyboardButton('Что может этот бот?')
keyboard_layout = [[key_1, key_2, key_3, key_4, key_5, key_2]]
main = ReplyKeyboardMarkup(keyboard_layout, resize_keyboard=True)


def greet_user(update, context):
    update.message.reply_text('Привет, я сделан для того, чтобы помогать тебе в уходе за твоим любимцем, я готов,'
                              ' задавай вопрос!😺', reply_markup=main)


def get_care(update, context):
    update.message.reply_text('С появлением в доме кошки многое в привычном распорядке дня поменяется.'
                              ' Питомца потребуется приучить к лотку и гигиеническим процедурам,'
                              ' наладить питание и позаботиться о том, чтобы внешняя среда была для него безопасной.'
                              ' Чтобы разобраться, как ухаживать за кошкой правильно,'
                              ' следуйте простым рекомендациям специалистов.😺')


def get_nutrition(update, context):
    update.message.reply_text('Скажите, сколько вашему коту лет?😺')


def character_description(update, context):
    update.message.reply_text('Характер у котика можно предугатать только когда он котенок😺')
    update.message.reply_text("Если вы с ним часто играете, не ругаете и не кричите на него, он вырастет дружелюбным😺")
    update.message.reply_text("Если ваш котенок охотится за вашими ногами, охотно играет и не сидит без дела,"
                              " то у вас будет кот-охотник😺")
    update.message.reply_text("Если вы часто гладите котенка, и воспитывете его, то он вырастете ласковым😺")
    update.message.reply_text("Если вы плохо относитесь к котенку, ругете его и кричите,"
                              " то он вырестете злым и своенравным котом😺")


def get_breed(update, context):
    update.message.reply_text('Для начинающих подойдут такие породы как "Сноу-шу", Британская короткошерстная",'
                              ' "Норвежская лесная", "Японский бобтейл", "Шотландская вислоухая"😺')
    update.message.reply_text("При должном воспитанииони могут вырасти дружелюбными")


def get_what_breed_of_cat(update, context):
    update.message.reply_text("Отлично, теперь отправте мне изображение с котом, а я с помощью AI определю его породу😺")


def get_help(update, context):
    update.message.reply_text("Я бот который помогает тебе в уходе за твоим любимцем, я подключен в размым мед сайтам,"
                              " форумам любителей котов, поэтому мои данные на 99.9% верны😺\n"
                              "Вот некоторые команды:\n"
                              "/start - запуск бота\n"
                              "/care - инфо об уходе\n"
                              "/nutrit - инфо о питании\n"
                              "/descrip - характер\n"
                              "/breed - все о породах\n"
                              "/wht_breed - определение какой породы кот")




def main():

    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("care", get_care))
    dp.add_handler(MessageHandler(Filters.regex('^(Уход)$'), get_care))
    dp.add_handler(CommandHandler("nutrit", get_nutrition))
    dp.add_handler(CommandHandler("descrip", character_description))
    dp.add_handler(CommandHandler("breed", get_breed))
    dp.add_handler(CommandHandler("wht_breed", get_what_breed_of_cat))
    dp.add_handler(CommandHandler("help", get_help))



    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
