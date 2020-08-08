from .database import Base

import datetime as dt
import sqlalchemy as sa


now = dt.datetime.now


class User(Base):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(32), nullable=False)
    first_name = sa.Column(sa.String(32))
    middle_name = sa.Column(sa.String(32))
    last_name = sa.Column(sa.String(32))
    is_active = sa.Column(sa.Boolean, default=False, nullable=False)
    created_at = sa.Column(sa.DateTime, default=now, nullable=False)
    updated_at = sa.Column(
        sa.DateTime, default=now, onupdate=now, nullable=False)

