from flask import Flask
from flask_restful import Api
from utils.db import db
from flask_cors import CORS
from config import DATABASE_CONNECTION_URI

from resources.sheet import SheetList, Sheet

app = Flask(__name__)
app.secret_key = "lwheoqiwub0b7qwdjqx"
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

CORS(app, resources={r"/*":{"origins":"*"}})

api = Api(app)

api.add_resource(SheetList, "/sheet")
api.add_resource(Sheet, "/sheet/<int:id>")

if __name__ == "__main__":
    app.run()