from flask import Flask
from flask import jsonify
from logic import add

app = Flask(__name__)


@app.route('/')
def hello():
    return {"message": "Hello"}

@app.route("/add/<num1>/<num2>")
def adder(num1, num2):
    result = add(num1,num2)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)