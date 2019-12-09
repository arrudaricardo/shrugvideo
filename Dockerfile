FROM python:3.7-alpine

WORKDIR /shrugvideo

RUN apk add sqlite
RUN apk add socat

COPY requirements.txt requirements.txt

# RUN python -m venv env
# RUN env/bin/pip install -r requirements.txt
# RUN env/bin/pip install gunicorn

RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY . .
# RUN chmod +x boot.sh

# gen database
RUN ["python", "-c", "from app.models import init_db; init_db()"]


COPY wsgi.py config.py boot.sh ./
ENV FLASK_APP main.py


EXPOSE 5000
CMD ["gunicorn", "--bind", ":5000", "wsgi:app"]