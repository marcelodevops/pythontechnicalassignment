# app.py
from flask import (
    Flask, render_template, redirect, url_for, flash, jsonify
)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import os
import subprocess
from flask_jwt_extended import JWTManager,create_acess_token,jwt_required,get_jwt_identity
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
JWT_SECRET = os.environ.get('JWT_SECRET')
jwt = JWTManager(app)

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
APP_VERSION = "1.0"
APP_DESCRIPTION = "marcelo's merck technical test."


# get last commit sha to show it in the healthcheck endpoint
def get_last_commit_sha():
    """Get the last commit SHA from Git or environment variable."""
    commit_sha = os.getenv("LAST_COMMIT_SHA")
    if commit_sha:
        return commit_sha
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"]
        ).strip().decode('utf-8')
    except Exception as e:
        return str(e)


# basic authentication form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


# main endpoint to dsplay form and authenticate
@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Welcome, {form.username.data}!', 'success')
        return redirect(url_for('login'))

    return render_template('login.html', form=form)


# healthcheck endpoint
@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    last_commit_sha = get_last_commit_sha()
    response = {
        "version": APP_VERSION,
        "description": APP_DESCRIPTION,
        "last_commit_sha": last_commit_sha
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
