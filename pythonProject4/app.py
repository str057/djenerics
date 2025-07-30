from flask import Flask
import requests

app = Flask(__name__)

# URL к файлу contacts.html в удаленном репозитории GitHub (raw-версия)
REMOTE_HTML_URL = 'https://raw.githubusercontent.com/ваш-username/ваш-репозиторитор/ветка/path/to/contacts.html'


@app.route('/', methods=['GET'])
@app.route('/<path:subpath>', methods=['GET'])
def contacts(subpath=None):
    try:
        # Загружаем HTML из удаленного репозитория
        response = requests.get(REMOTE_HTML_URL)
        response.raise_for_status()  # Проверяем на ошибки

        # Возвращаем HTML с правильным Content-Type
        return response.text, 200, {'Content-Type': 'text/html'}

    except requests.exceptions.RequestException as e:
        # В случае ошибки возвращаем сообщение об ошибке
        return f"Ошибка загрузки страницы: {str(e)}", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)