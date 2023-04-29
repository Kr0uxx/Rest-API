import flask
from flask import request, jsonify
from . import db_session
from .jobs import Jobs
from .users import User

blueprint = flask.Blueprint('jobs_api', __name__, template_folder='templates')


@blueprint.route('/api/jobs')
def get_jobs():
    try:
        db_sess = db_session.create_session()
        jobs = db_sess.query(Jobs).all()

        return jsonify({'jobs': [item.to_dict() for item in jobs]})
    except Exception as e:
        return jsonify({"error": e})