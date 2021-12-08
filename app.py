from flask import Flask, request
from prediction import predict_value
app = Flask(__name__)


@app.route("/prediction",methods=['GET'])
def test():
    stock = request.args.get("stock")
    return predict_value(stock)


if __name__ == '__main__':
    app.run()

