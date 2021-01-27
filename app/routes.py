from app import app
from flask import render_template
import secrets

@app.route("/")
def index():
	key = secrets.token_urlsafe()
	return render_template('index.html', key=key)