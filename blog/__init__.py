# coding: utf-8
from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
        'HOST': 'localhost',
        'PORT': 5433,
        'USERNAME': 'admin',
        'PASSWORD': '12345',
        'DB': 'flask_blog'
    }

db = MongoEngine(app)

if __name__ == '__main__':
    app.run()


def register_blueprints(app):
    from views import posts
    # регистрируем "болванку" для работы с постами
    app.register_blueprint(posts)

register_blueprints(app)
