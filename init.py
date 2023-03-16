import os

from flask import Flask
from flask_restful import Api
from flask.cli import load_dotenv

load_dotenv()

app = Flask(os.getenv('PROJECT_NAME'))

if __name__ == '__main__':
    Api(app)
    app.run()
