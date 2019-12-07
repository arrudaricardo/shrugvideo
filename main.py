#!flask/bin/python3
#from werkzeug.contrib.fixers import ProxyFix
from app import app
from os.path import isfile


# generate dabase 
if isfile('./app.db'):
	from app import models
	models.init_db()  #initialize a db with samples
		




if __name__ == "__main__":
	#app.wsgi_app = ProxyFix(app.wsgi_app)
	app.run()
