from flask import Flask, request
import requests

app = Flask(__name__)

# Замените на свой токен и ID чата
BOT_TOKEN = '6925633084:AAEbTGDSWJAAQaDl48X7QCeiHLN6MmljH8s'
CHAT_ID = '5682662110'

@app.route('/')
def index():
    # Получение IP-адреса пользователя
    user_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Отправка IP-адреса на Telegram
    message = f'IP-адрес пользователя: {user_ip}'
    telegram_url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': message}
    response = requests.post(telegram_url, json=payload)

    if response.status_code == 200:
        return 'IP успешно отправлен на Telegram!'
    else:
        return 'Ошибка при отправке IP на Telegram!'

if __name__ == '__main__':
    app.run(debug=True)
