from flask import Flask
import requests

app = Flask(__name__)

# Правильный URL к вашему файлу contacts.html
CONTACTS_HTML_URL = 'https://raw.githubusercontent.com/str057/Verstka/deve/contacts.html'


@app.route('/', methods=['GET'])
@app.route('/<path:subpath>', methods=['GET'])
def show_contacts(subpath=None):
    try:
        # Получаем HTML из GitHub
        response = requests.get(CONTACTS_HTML_URL)

        # Если файл не найден (404)
        if response.status_code == 404:
            return """
            <html>
                <body style="font-family: Arial, sans-serif; padding: 20px;">
                    <h1 style="color: #d9534f;">Ошибка 404</h1>
                    <p>Файл contacts.html не найден по указанному пути.</p>
                    <p>Проверьте URL: <a href="{url}" target="_blank">{url}</a></p>
                    <div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin-top: 20px;">
                        <h3>Возможные причины:</h3>
                        <ul>
                            <li>Файл был перемещен или переименован</li>
                            <li>Указана неправильная ветка репозитория</li>
                            <li>Файл не был закоммичен в репозиторий</li>
                        </ul>
                    </div>
                </body>
            </html>
            """.format(url=CONTACTS_HTML_URL), 404

        response.raise_for_status()  # Проверяем другие ошибки

        # Возвращаем HTML с правильным Content-Type
        return response.text, 200, {'Content-Type': 'text/html'}

    except requests.exceptions.RequestException as e:
        # Обработка других ошибок
        return """
        <html>
            <body style="font-family: Arial, sans-serif; padding: 20px;">
                <h1 style="color: #d9534f;">Ошибка загрузки</h1>
                <p>Произошла ошибка при загрузке страницы контактов.</p>
                <div style="background: #f8f9fa; padding: 15px; border-radius: 5px; margin-top: 20px;">
                    <p><strong>Ошибка:</strong> {error}</p>
                    <p><strong>URL:</strong> <a href="{url}" target="_blank">{url}</a></p>
                </div>
            </body>
        </html>
        """.format(error=str(e), url=CONTACTS_HTML_URL), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)