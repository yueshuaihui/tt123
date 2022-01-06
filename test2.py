import time
from flask import Flask

app = Flask(__name__)


@app.route("/t1")
def hello_world1():
    return {"code": 1000, "msg": "success", "data": [1, 2, 3]}


@app.route("/t2")
def hello_world2():
    return {"code": 1000, "msg": "success", "data": [4, 5, 6]}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
