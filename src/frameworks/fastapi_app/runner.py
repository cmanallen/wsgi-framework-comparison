from src.lib.models import User
from src.lib.views import UserSchema

import databases
import json
import fastapi
import time


app = fastapi.FastAPI()
database = databases.Database('sqlite:///test.db')


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get('/')
def index():
    return "Hello, world!"


@app.get('/wait')
def wait():
    time.sleep(0.025)
    return "Hello, world!"


@app.get('/real')
async def real():
    # "Authorize"
    user = await database.fetch_one(User.__table__.select().where(User.id == 1))

    # Dump results
    users = await database.fetch_all(User.__table__.select())
    result = UserSchema().dump(users, many=True)
    return json.dumps(result)
