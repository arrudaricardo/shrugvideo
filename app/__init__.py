from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

# # generate dabase 
# if isfile('./app.db'):
# 	from app import models
# 	models.init_db()  #initialize a db with samples

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app import routes, models 
