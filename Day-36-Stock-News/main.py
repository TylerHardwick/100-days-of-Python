import requests
from twilio.rest import Client
import os


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API = os.environ.get("STOCK_API")
NEWS_API = os.environ.get("NEWS_API")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
MY_NUM = 123
SEND_NUM = 456


stock_parameters = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_API
}

stock_request = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
stock_request.raise_for_status()
stock_data = stock_request.json()
stock_data_dict = stock_data["Time Series (Daily)"]
current_day = list(stock_data_dict)[0]
previous_day = list(stock_data_dict)[1]
close_value_today = float(stock_data_dict[current_day]["4. close"])
close_value_yday = float(stock_data_dict[previous_day]["4. close"])
percentage_dif = (close_value_today-close_value_yday)/close_value_yday*100
if percentage_dif >= 2 or percentage_dif <= -2:

    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API
    }

    news_request = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_request.raise_for_status()
    news_articles = news_request.json()
    news = news_articles["articles"][0]

    if percentage_dif > 0:
        message_body = f"{STOCK}: {round(percentage_dif, 2)}%📈 \n Headline: {news['title']} \n Source: {news['url']}"
    else:
        message_body = f"{STOCK}: {round(percentage_dif, 2)}%📉 \n Headline: {news['title']} \n Source: {news['url']}"

    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body = message_body,
        from_ = SEND_NUM,
        to = MY_NUM,
    )
    print(message.status)


