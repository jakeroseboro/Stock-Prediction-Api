import datetime
from dateutil.relativedelta import relativedelta
import yfinance as yf

today = datetime.datetime.today();
two_months_ago = today - relativedelta(months=2)
start = str(two_months_ago).split(' ')[0]
end = str(today).split(' ')[0];


def test_date(ticker):
    data = yf.download(ticker, start, end)
    data = data[["Adj Close"]]
    data = data.dropna()
    print(data)

    return str(data)
