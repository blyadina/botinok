#БОТА СОЗДАЛ TG: @sugarhuman
import requests
import threading
from datetime import datetime, timedelta
from telebot import TeleBot
import telebot
import time
#Для первого урока на курсе Hacking

# Нужно вписать токет своего бота.
TOKEN = '923623654:AAGpFsjmb2xHZx5EV1ZcWM_M-y9rq4tlRGc'

# Можно уменьшить количество потоков-исполнителем этой переменной. Не знаю возможности системы так что ставлю 20
THREADS_LIMIT = 400

chat_ids_file = 'chat_ids.txt'

# Нужно вписать айди админского чата
ADMIN_CHAT_ID = Твой Ид

# Эти переменные лучше не менять
users_amount = [0]
threads = list()
THREADS_AMOUNT = [0]
types = telebot.types
bot = TeleBot(TOKEN)
running_spams_per_chat_id = []


def save_chat_id(chat_id):
    "Функция добавляет чат айди в файл если его там нету"
    chat_id = str(chat_id)
    with open(chat_ids_file,"a+") as ids_file:
        ids_file.seek(0)

        ids_list = [line.split('\n')[0] for line in ids_file]

        if chat_id not in ids_list:
            ids_file.write(f'{chat_id}\n')
            ids_list.append(chat_id)
            print(f'New chat_id saved: {chat_id}')
        else:
            print(f'chat_id {chat_id} is already saved')
        users_amount[0] = len(ids_list)
    return


def send_message_users(message):

    def send_message(chat_id):
        data = {
            'chat_id': chat_id,
            'text': message
        }
        response = requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data=data)

    with open(chat_ids_file, "r") as ids_file:
        ids_list = [line.split('\n')[0] for line in ids_file]

    [send_message(chat_id) for chat_id in ids_list]


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    boom = types.KeyboardButton(text='🔥💣БОМБЕР')
    stop = types.KeyboardButton(text='Стоп Спам')
    info = types.KeyboardButton(text='ℹ️Информация')
    stats = types.KeyboardButton(text='📈Статистика')
    donat = types.KeyboardButton(text='💰Поддержать')
    piar = types.KeyboardButton(text='💸 Реклама')
    faq = types.KeyboardButton(text='FAQ / Соглашение')

    buttons_to_add = [boom, stop, info, stats, donat, piar, faq]

    if int(message.chat.id) == ADMIN_CHAT_ID:
        buttons_to_add.append(types.KeyboardButton(text='Рассылка'))

    keyboard.add(*buttons_to_add)
    bot.send_message(message.chat.id, 'Добро пожаловать🙋‍♂!\nНаш форум: ТУТ ВАШЕ.ru\nНаш чат в ТГ:  ТУТ ВАШЕ\nВыберите действие:',  reply_markup=keyboard)
    save_chat_id(message.chat.id)


def send_for_number(phone):
        request_timeout = 0.00001
        requests.post('Тут сервисы'), data{ }

def start_spam(chat_id, phone_number, force):
    running_spams_per_chat_id.append(chat_id)

    if force:
        msg = f'Спам запущен на неограниченое время для номера +{phone_number}'
    else:
         msg = f'Спам запущен на 20 минут на номер +{phone_number}'

    bot.send_message(chat_id, msg)
    end = datetime.now() + timedelta(minutes = 20)
    while (datetime.now() < end) or (force and chat_id==ADMIN_CHAT_ID):
        if chat_id not in running_spams_per_chat_id:
            break
        send_for_number(phone_number)
    bot.send_message(chat_id, f'Спам на номер {phone_number} завершён')
    THREADS_AMOUNT[0] -= 1 # стояло 1
    try:
        running_spams_per_cзнhat_id.remove(chat_id)
    except Exception:
        pass


def spam_handler(phone, chat_id, force):
    if int(chat_id) in running_spams_per_chat_id:
        bot.send_message(chat_id, 'Вы уже начали рассылку спама. Дождитесь окончания или нажмите Стоп Спам и поробуйте снова')
        return

    # Если количество тредов меньше максимального создается новый который занимается спамом
    if THREADS_AMOUNT[0] < THREADS_LIMIT:
        x = threading.Thread(target=start_spam, args=(chat_id, phone, force))
        threads.append(x)
        THREADS_AMOUNT[0] += 1
        x.start()
    else:
        bot.send_message(chat_id, 'Сервера сейчас перегружены. Попытайтесь снова через несколько минут')
        print('Максимальное количество тредов исполняется. Действие отменено.')


@bot.message_handler(content_types=['text'])
def handle_message_received(message):
    chat_id = int(message.chat.id)
    text = message.text

    if text == 'ℹ️Информация':
        bot.send_message(chat_id, 'Создатель бота: @sugarhuman\nПо вопросам сотрудничества обращаться в ЛС к создателю бота')

    elif text == '🔥💣БОМБЕР':
        bot.send_message(chat_id, 'Введите номер без + в формате:\n🇺🇦 380xxxxxxxxx\n🇷🇺 79xxxxxxxxx')

    elif text == '📈Статистика':
        bot.send_message(chat_id, f'📊Статистика отображается в реальном времени📡!\nПользователей🙎‍♂: {users_amount[0]}\nСервисов для RU🇷🇺: 25\nСервисов для UK🇺🇦: 10\nБот запущен:07.11.2019')

    elif text == '💰Поддержать':
        bot.send_message(chat_id, 'Ребята, кто может материально помочь на развитие бота\nВот реквизиты\nEasyPay 62733731 ')
    
    elif text == '💸 Реклама':
        bot.send_message(chat_id, 'В Нашем Боте @SMSspamatackRobot рассылка стоит  150 рублей\nЕё получат все пользователи бота\nПо вопросам покупки писать @sugarhuman')    

    elif text == 'Рассылка' and chat_id==ADMIN_CHAT_ID:
        bot.send_message(chat_id, 'Введите сообщение в формате: "РАЗОСЛАТЬ: ваш_текст" без кавычек')

    elif text == 'FAQ / Соглашение':
        bot.send_message(chat_id, '"SMS Spam Bomber++" предлагается Вашему вниманию при условии Вашего полного согласия со всеми правилами. При доступе или использовании данного сервиса каким-либо образом Вы даете согласие действовать в рамках Пользовательского соглашения\nПОЛЬЗОВАТЕЛЬСКОЕ СОГЛАШЕНИЕ\n1.Настоящее Пользовательское соглашение (далее – Соглашение) относится к сервису информационно-развлекательного ресурса "SMS Spam Bomber++"\n2.Доступ к сервису предоставляется на бесплатной основе.\n3."SMS Spam Bomber++" сервис предназначен исключительно для развлекательных целей.\n4.На Администрацию сервиса не возлагается каких-либо обязательств перед пользователями.\n5.Администрация сайта не принимает встречные предложения от Пользователей относительно изменений настоящего Пользовательского соглашения.\n6.Администрация сервиса "SMS Spam Bomber++" Не несет ответственности за причиненный ущерб третьим лицам попавших под влияние сервиса.\nСпасибо за внимание!')

    
    elif text == 'Стоп Спам':
        if chat_id not in running_spams_per_chat_id:
            bot.send_message(chat_id, 'Вы еще не начинали спам')
        else:
            running_spams_per_chat_id.remove(chat_id)

    elif 'РАЗОСЛАТЬ: ' in text and chat_id==ADMIN_CHAT_ID:
        msg = text.replace("РАЗОСЛАТЬ: ","")
        send_message_users(msg)

    elif len(text) == 11:
        phone = text
        spam_handler(phone, chat_id, force=False)


    elif len(text) == 12:
        phone = text
        spam_handler(phone, chat_id, force=False)



    elif len(text) == 12 and chat_id==ADMIN_CHAT_ID and text[0]=='_':
        phone = text[1:]
        spam_handler(phone, chat_id, force=True)

    else:
        bot.send_message(chat_id, f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')
        print(f'Номер введен неправильно. Введено {len(text)} символов, ожидается 11')

if __name__ == '__main__':
    bot.polling(none_stop=True)
# Реклама - рассылка:
Цена: 100₽
Каждый пользователь получит уведомление с вашим текстом.

24 часа (1 день) + 1 рассыка - 150₽
48 часов (2 дня) + 1 рассыка - 250₽
120 часов (5 дней) + 1 рассыка - 400₽


Купить: @sugarhuman