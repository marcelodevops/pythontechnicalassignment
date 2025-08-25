# app.py
from flask import (
    Flask, render_template, redirect, url_for, flash, jsonify, flash, request
)
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from functools import wraps
import os
import subprocess
import jwt

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')


APP_VERSION = "1.0"
APP_DESCRIPTION = "marcelo's merck technical test."


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except Exception:
            return jsonify({'message': 'Invalid token'}), 403

        return func(*args, **kwargs)

    return decorated


@app.route('/private')
@token_required
def auth():
    return 'JWT is verified. Welcome to your private page!'


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
