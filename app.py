from flask import Flask, request, render_template, redirect, url_for, flash
from prediction import predict_value
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
app = Flask(__name__)


@app.route("/prediction",methods=['GET'])
def test():
    stock = request.args.get("stock")
    return predict_value(stock)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
