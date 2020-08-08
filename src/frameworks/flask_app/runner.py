from src.lib.models import User
from src.lib.views import UserSchema

import flask
import json
import sqlalchemy as sa
import time


app = flask.Flask(__name__)

engine = sa.create_engine('sqlite:///test.db')
session_factory = sa.orm.scoped_session(
    sa.orm.sessionmaker(bind=engine),
    scopefunc=flask._app_ctx_stack.__ident_func__)


@app.route('/')
def index():
    return "Hello, world!"


@app.route('/wait')
def wait():
    time.sleep(0.025)
    return "Hello, world!"


@app.route('/real')
def real():
    session = session_factory()

    # "Authorize"
    user = session.execute(User.__table__.select().where(User.id == 1))

    # Dump results
    users = session.execute(User.__table__.select())
    result = UserSchema().dump(users, many=True)

    session_factory.remove()
    return json.dumps(result)
