import os
from flask import Flask

STATIC_DIR = os.path.abspath('../django-secret-key-generator/static/')
app = Flask(__name__, static_folder=STATIC_DIR)

if __name__ == "__main__":
	app.run(debug=False, host='0.0.0.0')

from app import routes
