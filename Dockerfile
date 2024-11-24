FROM python:3.9-slim

# Встановлюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо залежності і встановлюємо їх
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Копіюємо код додатку
COPY . .

# Вказуємо команду для запуску додатку
CMD ["python", "app.py"]
