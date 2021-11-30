from flask import request, Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from SQLALCHEMY_DATABASE_URI import SQLALCHEMY_DATABASE_URI
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# string SQLALCHEMY_DATABASE_URI = "mysql://'seu_usuario':'sua_senha'@localhost/'seu_db'"

db = SQLAlchemy(app)


class Example(db.Model):
    __tablename__ = 'example'
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.Unicode)

    def __init__(self, data):
        self.data = data


@app.route('/', methods=['GET'])
def get():
    home = {"Get": "SucessFull"}
    return jsonify(home)


@app.route('/post', methods=['POST'])
def get_json():
    data = request.get_json()
    name = data["name"]
    new_insertion = Example(str(name))
    db.session.add(new_insertion)
    db.session.commit()
    return jsonify(data)


if __name__ == "__main__":
    app.run()
