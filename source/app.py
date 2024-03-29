import threading
import time

from flask import Flask, request, render_template, jsonify

from funcs.funcs import start_external_function, stop_external_function

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'start' in request.form:
            stop_external_function()
            with open("temp.txt", "w") as file:
                file.write(f"{0} {0}")
            if request.form['count'] and request.form['timer']:
                # Получаем значение из поля ввода
                count = int(request.form['count'])
                timer = int(request.form['timer'])
                # Запускаем внешнюю функцию
                time.sleep(2)
                my_thread = threading.Thread(target=start_external_function, args=(count, timer), daemon=True)
                my_thread.start()

        elif 'stop' in request.form:
            # Останавливаем внешнюю функцию
            stop_external_function()
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start():
    count = int(request.form['count'])
    start_external_function(count)
    return 'External function started'


@app.route('/stop', methods=['POST'])
def stop():
    stop_external_function()
    return 'External function stopped'


@app.route('/get_form')
def get_form():
    with open('temp.txt', "r") as file:
        data = list(map(int, file.read().strip().split()))

    return jsonify(result=data)


if __name__ == '__main__':
    app.run(debug=True)
