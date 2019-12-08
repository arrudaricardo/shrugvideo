#!/bin/sh
# source env/bin/activate
# exec gunicorn -b 0.0.0.0:5000 wsgi:app
exec gunicorn --bind :5000 wsgi:app