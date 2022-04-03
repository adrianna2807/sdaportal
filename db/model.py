from datetime import datetime

from faker import Faker
from sqlalchemy import Column, String, Integer, DateTime, Text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    reg_date = Column(DateTime, nullable=False, default=datetime.now)

    def __repr__(self):
        return f"User({self.id}, {self.first_name}, {self.last_name}, {self.email})"

    @staticmethod
    def create_fake_user():
        fake = Faker()
        return User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email()
        )


def create_fake_users(session, count=100):
    users_generated = 0
    while users_generated < count:
        try:
            session.add(User.create_fake_user())
            session.commit()
        except IntegrityError:
            session.rollback()
            continue
        users_generated += 1


class Hashtag(Base):
    __tablename__ = "hashtags"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"Hashtag({self.id}, {self.name})"

    @staticmethod
    def creat_fake_hashtag():
        fake = Faker()
        return Hashtag(name=fake.word())


def create_fake_hashtags(session, count=100):
    hashtags_generated = 0
    while hashtags_generated < count:
        try:
            session.add(Hashtag.creat_fake_hashtag())
            session.commit()
        except IntegrityError:
            session.rollback()
            continue
        hashtags_generated += 1


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False, unique=True)
    content = Column(Text, nullable=False, unique=True)
    publication_date = Column(DateTime, nullable=False, default=datetime.now)

    author_id = Column(Integer, nullable=False)