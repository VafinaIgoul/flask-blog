# coding: utf-8
import os
import sys

from flask_script import Manager
from flask_script import Server
from blog import app

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

manager = Manager(app)

# Включение по умолчанию отладчика и перезагрузки
manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host='0.0.0.0')
)

if __name__ == "__main__":
    manager.run()
