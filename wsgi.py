#!flask/bin/python3
from werkzeug.contrib.fixers import ProxyFix
from app import app


if __name__ == "__main__":
	#app.wsgi_app = ProxyFix(app.wsgi_app)
	app.run()
