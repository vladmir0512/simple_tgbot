import requests # Модуль позволяет отправлять post, get и прочие запросы
import misc # Файлик, в котором я храню токен
import json # Библиотека для работы с json, конкретно метод dump()
from time import sleep
#https://api.telegram.org/bot5540149986:AAE0qQjVgvobPBOfVxSqOBueeGC2Vc9PWrs/sendmessage?chat_id=929644995&text=hi


token = misc.token # Подгружаем токен из модуля, в котором он хранится
URL = 'https://api.telegram.org/bot' + token + '/' # Создаем универсальную ссылку для дальнейших запросов
global last_update_id
last_update_id = 0

# Получаем данные бота в виде json
def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url) 
    return r.json() 


def get_message():
    data = get_updates()

    last_obj = data['result'][-1]
    current_update_id = last_obj["update_id"]

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = last_obj["message"]["chat"]["id"]
        message_text = last_obj["message"]["text"]

        message = {'chat_id':chat_id,
                  'text': message_text}
        return message

    return None


def main():


    while 1: 
        answer = get_message()
        if answer != None:
            chat_id = answer["chat_id"]
            text = answer['text']

            if 'кашу' in text:
                send_message(chat_id, 'Какую?')
                sleep(2)
        else:
            continue

def send_message(chat_id, text='Wait a second, please...'):
    url = URL + f'sendmessage?chat_id={chat_id}&text={text}'
    requests.get(url)

if __name__ == '__main__':
    main()
