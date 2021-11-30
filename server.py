from flask import request, Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    home = {"Get": "SucessFull"}
    return jsonify(home)


@app.route('/post', methods=['POST'])
def get_json():
    data = request.get_json()
    return jsonify(data)


if __name__ == "__main__":
    app.run()
