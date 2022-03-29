from flask import Flask, render_template, url_for, request, redirect
import datetime
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def update_ticker(Link):

    headers = {
        'user agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.135 Safari/537.36"}
    html = requests.get(Link, headers)
    soup = BeautifulSoup(html.content, 'html.parser')
    convert = soup.findAll('div', {'class': 'YMlKec fxKbKc'})
    price = str(convert[0].text[1:])
    return price




@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")



@app.route('/msc-market')
def rumarket():
    LKOH = update_ticker("https://www.google.com/finance/quote/LKOH:MCX")
    GAZP = update_ticker("https://www.google.com/finance/quote/GAZP:MCX")
    SBER = update_ticker("https://www.google.com/finance/quote/SBER:MCX")
    YNDX = update_ticker("https://www.google.com/finance/quote/YNDX:MCX")
    ROSN = update_ticker("https://www.google.com/finance/quote/ROSN:MCX")
    TCSG = update_ticker("https://www.google.com/finance/quote/TCSG:MCX")
    VKCO = update_ticker("https://www.google.com/finance/quote/VKCO:MCX")
    AFLT = update_ticker("https://www.google.com/finance/quote/AFLT:MCX")
    VTBR = update_ticker("https://www.google.com/finance/quote/VTBR:MCX")
    MGNT = update_ticker("https://www.google.com/finance/quote/MGNT:MCX")
    dt = datetime.datetime.now()
    return render_template("msk-market.html", time=dt.strftime('%d.%m.%Y %H:%M:%S'), LKOH=LKOH, GAZP=GAZP,
                           SBER=SBER, YNDX=YNDX, ROSN=ROSN, TCSG=TCSG, VKCO=VKCO,
                           AFLT=AFLT, VTBR=VTBR, MGNT=MGNT)


# Компании, акции которых торгуются на СПБ бирже
@app.route('/spb-market')
def market():
    AAPL = update_ticker("https://www.google.com/finance/quote/AAPL:NASDAQ")
    TSLA = update_ticker("https://www.google.com/finance/quote/TSLA:NASDAQ")
    BABA = update_ticker("https://www.google.com/finance/quote/BABA:NYSE")
    MSFT = update_ticker("https://www.google.com/finance/quote/MSFT:NASDAQ")
    AMZN = update_ticker("https://www.google.com/finance/quote/AMZN:NASDAQ")
    META = update_ticker("https://www.google.com/finance/quote/FB:NASDAQ")
    BA = update_ticker("https://www.google.com/finance/quote/BA:NYSE")
    NVDA = update_ticker("https://www.google.com/finance/quote/NVDA:NASDAQ")
    PYPL = update_ticker("https://www.google.com/finance/quote/PYPL:NASDAQ")
    F = update_ticker("https://www.google.com/finance/quote/F:NYSE")
    dt = datetime.datetime.now()
    return render_template("spb-market.html", time=dt.strftime('%d.%m.%Y %H:%M:%S'), AAPL=AAPL, TSLA=TSLA, BABA=BABA,
                           MSFT=MSFT, AMZN=AMZN, META=META, BA=BA, NVDA=NVDA, PYPL=PYPL, F=F)




if __name__ == "__main__":
    app.run(debug=True)