import datetime

import numpy
from dateutil.relativedelta import relativedelta
import yfinance as yf
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

today = datetime.datetime.today();
two_months_ago = today - relativedelta(months=2)
tmrw = today + relativedelta(days=1)

start = str(two_months_ago).split(' ')[0]
end = str(today).split(' ')[0];
predict = str(tmrw).split(' ')[0];


def predict_value(ticker):
    data = yf.download(ticker, start, end)
    data = data[["Adj Close"]]
    data = data.dropna()
    data = data.reset_index()
    data = data.drop("Date", 1)

    X = data.index.values
    X = X.reshape(-1,1)
    Y = data.iloc[:, 0].values

    idx = numpy.float64(len(X.tolist()))

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
    regressor = LinearRegression()
    regressor.fit(X_train, Y_train)
    X_predict = [idx]

    y_predict = regressor.predict([X_predict])
    return str(y_predict)
