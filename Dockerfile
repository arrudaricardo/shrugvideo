FROM python:3.7-alpine

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m venv env
RUN env/bin/pip install -r requirements.txt
RUN env/bin/pip install gunicorn

COPY . app
RUN chmod +x boot.sh

COPY config.py boot.sh ./
ENV FLASK_APP main.py

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]