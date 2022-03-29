from flask import Flask, render_template, url_for, request, redirect
import datetime
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)



def update_ticker(Link, rank):

    headers = {
        'user agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.135 Safari/537.36"}
    html = requests.get(Link, headers)
    soup = BeautifulSoup(html.content, 'html.parser')
    convert = soup.findAll('div', {'class': 'YMlKec fxKbKc'})
    if rank == 0:
        price = str(convert[0].text[0:])
    elif rank == 1:
        price = str(convert[0].text[1:])

    return price




@app.route('/')
@app.route('/home')
def index():
    UsdRub = update_ticker("https://www.google.com/finance/quote/USD-RUB", 0)
    EurRub = update_ticker("https://www.google.com/finance/quote/EUR-RUB", 0)
    return render_template("index.html", UsdRub=UsdRub, EurRub=EurRub)

@app.route('/about')
def about():
    return render_template("about.html")


# Компании, акции которых торгуются на Мск бирже
@app.route('/msc-market')
def rumarket():
    LKOH = update_ticker("https://www.google.com/finance/quote/LKOH:MCX", 1)
    GAZP = update_ticker("https://www.google.com/finance/quote/GAZP:MCX", 1)
    SBER = update_ticker("https://www.google.com/finance/quote/SBER:MCX", 1)
    YNDX = update_ticker("https://www.google.com/finance/quote/YNDX:MCX", 1)
    ROSN = update_ticker("https://www.google.com/finance/quote/ROSN:MCX", 1)
    TCSG = update_ticker("https://www.google.com/finance/quote/TCSG:MCX", 1)
    VKCO = update_ticker("https://www.google.com/finance/quote/VKCO:MCX", 1)
    AFLT = update_ticker("https://www.google.com/finance/quote/AFLT:MCX", 1)
    dt = datetime.datetime.now()
    return render_template("msk-market.html", time=dt.strftime('%d.%m.%Y %H:%M:%S'), LKOH=LKOH, GAZP=GAZP,
                           SBER=SBER, YNDX=YNDX, ROSN=ROSN, TCSG=TCSG, VKCO=VKCO,
                           AFLT=AFLT)


# Компании, акции которых торгуются на СПБ бирже
@app.route('/spb-market')
def market():
    AAPL = update_ticker("https://www.google.com/finance/quote/AAPL:NASDAQ", 1)
    TSLA = update_ticker("https://www.google.com/finance/quote/TSLA:NASDAQ", 1)
    BABA = update_ticker("https://www.google.com/finance/quote/BABA:NYSE", 1)
    MSFT = update_ticker("https://www.google.com/finance/quote/MSFT:NASDAQ", 1)
    AMZN = update_ticker("https://www.google.com/finance/quote/AMZN:NASDAQ", 1)
    META = update_ticker("https://www.google.com/finance/quote/FB:NASDAQ", 1)
    BA = update_ticker("https://www.google.com/finance/quote/BA:NYSE", 1)
    NVDA = update_ticker("https://www.google.com/finance/quote/NVDA:NASDAQ", 1)
    PYPL = update_ticker("https://www.google.com/finance/quote/PYPL:NASDAQ", 1)
    F = update_ticker("https://www.google.com/finance/quote/F:NYSE", 1)
    dt = datetime.datetime.now()
    return render_template("spb-market.html", time=dt.strftime('%d.%m.%Y %H:%M:%S'), AAPL=AAPL, TSLA=TSLA, BABA=BABA,
                           MSFT=MSFT, AMZN=AMZN, META=META, BA=BA, NVDA=NVDA, PYPL=PYPL, F=F)




if __name__ == "__main__":
    app.run(debug=True)