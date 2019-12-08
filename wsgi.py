#!flask/bin/python3
#from werkzeug.contrib.fixers import ProxyFix
from app import app
from os.path import isfile


		

print('stating flask application')


if __name__ == "__main__":
	#app.wsgi_app = ProxyFix(app.wsgi_app)
	app.run()
