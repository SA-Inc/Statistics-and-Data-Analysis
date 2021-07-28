import sys
import json
import requests
import datetime
import smtplib
import ssl


# get Secret Data
def get_env(path):
    with open(path) as f:
        return json.load(f)

env = get_env('.env.json')

def date_validate(date, format):
    try:
        datetime.datetime.strptime(date, format)
        return True
    except ValueError:
        return False

def read_stock_tickers(ticker_file):
    try:
        with open(ticker_file) as file:
            ticker_array = file.readlines()
        return [x.strip() for x in ticker_array]
    except OSError:
        print('Could not open/read file')
        sys.exit()

def print_stock_tickers(tickers_array):
    print('Your Tikers:')
    for i in range(len(tickers_array)):
        print(tickers_array[i])
    print('')

def write_stock_to_file(stock_message, from_date, to_date):
    with open('stock_result_{}_{}.html'.format(from_date, to_date), 'w', encoding='utf-8') as file:
        file.write(stock_message)
        print('File stock_result_{}_{}.html created'.format(from_date, to_date))

def send_email(message):
    smtpServer = env['SMTP_SERVER']
    smtpPort = env['SMTP_PORT']
    fromEmail = env['FROM_EMAIL']
    fromPassword = env['FROM_PASSWORD']
    toEmail = env['TO_EMAIL']

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtpServer, smtpPort, context = context) as server:
        server.login(fromEmail, fromPassword)
        server.sendmail(fromEmail, toEmail, message)



Finnhub_API = env['FINNHUB_API']
from_date = ''
to_date = ''
stocks = read_stock_tickers('stock_tickers.txt')
stock_message = ''

print_stock_tickers(stocks)

print('From Date (yyyy-mm-dd), if skip - yesterday: ')
date = input()
if date == '':
    from_date = datetime.datetime.now() - datetime.timedelta(days = 1)
    from_date = from_date.strftime("%Y-%m-%d")
elif date_validate(date, '%Y-%m-%d') == True:
    from_date = date
else:
    print('Invalid Date Format')
    sys.exit()

print('To Date (yyyy-mm-dd), if skip - today: ')
date = input()
if date == '':
    to_date = datetime.datetime.now()
    to_date = to_date.strftime("%Y-%m-%d")
elif date_validate(date, '%Y-%m-%d') == True:
    to_date = date
else:
    print('Invalid Date Format')
    sys.exit()


stock_message += 'Subject: Stock News<br><br>'
stock_message += 'From: {}<br>'.format(from_date)
stock_message += 'To: {}<br>'.format(to_date)
stock_message += '<br>'

for stock in stocks:
    print('Processing {}'.format(stock))
    stock_response = requests.get('https://finnhub.io/api/v1/company-news?symbol={}&from={}&to={}&token={}'.format(stock, from_date, to_date, Finnhub_API))
    stock_json = stock_response.json()
    stock_message += '<b>{}</b>, Total News: <i>{}</i><br><br>'.format(stock, len(stock_json))

    for i in stock_json:
        stock_message += '<b>{0}</b><br>{1}<br><i>Source: <a href="{3}" target="_blank">{2}</a></i>'.format(i['headline'], i['summary'], i['source'], i['url'])
        stock_message += '<br><br>'
    stock_message += '<br><br>'



write_stock_to_file(stock_message, from_date, to_date)
# send_email(stock_message)