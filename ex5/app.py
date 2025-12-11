import logging
import socket
import time
from flask import Flask, jsonify, request

app = Flask(__name__)


UDP_IP = "127.0.0.1"
UDP_PORT = 8125
LOG_FILE = 'app.log'

# Змінні для статистики
start_time = time.time()
request_count = 0


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)



def send_to_statsd(message):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message.encode('utf-8'), (UDP_IP, UDP_PORT))
    except Exception as e:
        print(f"Не вдалося відправити UDP: {e}")



@app.before_request
def before_request():
    global request_count
    request_count += 1



@app.errorhandler(Exception)
def handle_exception(e):

    logging.exception("Критична помилка під час обробки запиту")

    error_msg = f"ERROR: {type(e).__name__} - {str(e)}"
    send_to_statsd(error_msg)

    return "Internal Server Error", 500




@app.route('/')
def index():
    logging.info("Оброблено запит на головну сторінку")
    return "Сервіс працює"


@app.route('/error')
def trigger_error():
    logging.warning("Хтось намагається викликати помилку...")

    return str(1 / 0)


@app.route('/status')
def status():
    uptime = time.time() - start_time
    logging.info("Запит на отримання статусу")

    data = {
        "uptime_seconds": round(uptime, 2),
        "request_count": request_count,
        "status": "OK"
    }
    return jsonify(data)


if __name__ == '__main__':
    print("🚀 Запуск Flask сервера...")
    app.run(port=5000, debug=False)