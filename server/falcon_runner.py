from lib.models import User
from lib.views import UserSchema

import falcon
import json
import sqlalchemy as sa
import time


engine = sa.create_engine('sqlite:///test.db')
session_factory = sa.orm.scoped_session(sa.orm.sessionmaker(bind=engine))


class Index:

    def on_get(self, request, response):
        response.status = falcon.HTTP_200
        response.body = "Hello, world!"


class Wait:

    def on_get(self, request, response):
        time.sleep(0.025)
        response.status = falcon.HTTP_200
        response.body = "Hello, world!"


class Real:

    def on_get(self, request, response):
        session = session_factory()

        # "Authorize"
        user = session.execute(User.__table__.select().where(User.id == 1))

        # Dump results
        users = session.execute(User.__table__.select())
        result = UserSchema().dump(users, many=True)
        result = json.dumps(result)

        response.status = falcon.HTTP_200
        response.body = result

        session_factory.remove()


app = falcon.API()
app.add_route('/', Index())
app.add_route('/wait', Wait())
app.add_route('/real', Real())
