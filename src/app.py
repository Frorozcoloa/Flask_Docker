from flask import Flask, jsonify

from users import  users


app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    return jsonify({'reponse':"Hello World"})

@app.route('/users', methods=['GET'])
def userHandler():
    return jsonify({"Users": users})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)