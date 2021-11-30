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


@app.route('/user/id', methods=['GET'])
# /user/id?id=
def get_by_id():
    user_id = request.args.get('id')
    user = Example.query.filter_by(id=user_id).first()
    user_name = {"user": "User don't exist"}
    if user:
        user_name = {"user": user.data}
    return jsonify(user_name)


@app.route('/user/name', methods=['GET'])
# /user/name?name=
def get_by_name():
    name = request.args.get('name')
    output = []
    users = Example.query.all()
    for user in users:
        if name in user.data:
            output.append({f"user_id: {user.id}",
                          f"user_name: {user.data}"})
    return str(output)


@app.route('/user', methods=['PUT'])
# /user?id=
def put_by_id():
    user_id = request.args.get('id')
    user = Example.query.filter_by(id=user_id).first()
    data = request.get_json()
    name = data["name"]
    user_name = {"user": "User don't exist"}
    if user:
        user.data = name
        db.session.commit()
        return jsonify({"user": name})
    return jsonify(user_name)


@app.route('/post', methods=['POST'])
def post_user():
    data = request.get_json()
    name = data["name"]
    new_insertion = Example(str(name))
    db.session.add(new_insertion)
    db.session.commit()
    return jsonify(data)


if __name__ == "__main__":
    app.run()
