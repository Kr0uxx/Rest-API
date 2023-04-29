from data import jobs_api
import data.db_session as session
from flask import Flask, make_response, request, jsonify
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

account = ''


if __name__ == '__main__':
    session.global_init("db/blogs.db")
    db_session = session.create_session()
    app.register_blueprint(jobs_api.blueprint)

    app.run(port=8080, host='127.0.0.1')
