from uuid import uuid4
from sqlalchemy import Column, Text
from sqlalchemy.dialects.postgresql import UUID

from app.app import db


class Account(db.Model):
    __tablename__ = "accounts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(Text(), unique=True, nullable=False)
    country = Column(Text(), nullable=False)
    default_currency = Column(Text(), nullable=False)
