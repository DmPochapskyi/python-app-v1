from flask import Flask, Response, request
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Визначення метрики для підрахунку запитів
REQUEST_COUNT = Counter('app_requests_total', 'Total HTTP requests', ['method', 'endpoint'])

@app.before_request
def before_request_func():
    # Лічильник HTTP-запитів
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()

@app.route('/')
def hello_world():
    return {"message": "Hello, World!"}

@app.route('/metrics')
def metrics():
    # Генерація метрик у форматі Prometheus
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
