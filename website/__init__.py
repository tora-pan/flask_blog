from flask import Flask
from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'someRandomSecretKeyStringHere12345'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True, nullable=False)
    email = Column(String(35), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow)

    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'


engine = create_engine('postgresql://travispandos:tatsulok1@localhost:5432/flask_blog')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# user = User(1234, 'tora_pan2', 'travis.pandos2@gmail.com', 'password1')
# session.add(user)
# session.commit()

results = session.query(User).all()
print([result.username for result in results])
