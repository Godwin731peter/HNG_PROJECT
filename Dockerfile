FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#RUN SECRET_KEY=dummy-build-key python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["sh", "-c", "gunicorn hng_task.wsgi:application --bind 0.0.0.0:$PORT"]