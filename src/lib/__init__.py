from .database import Base
from .models import User

import sqlalchemy as sa


def mock():
    engine = sa.create_engine('sqlite:///test.db')
    Base.metadata.create_all(engine)

    session = sa.orm.sessionmaker(bind=engine)
    session = session()

    for i in range(10):
        user = User(username=str(i))
        session.add(user)
    session.commit()
