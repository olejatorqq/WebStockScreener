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


LKOH = update_ticker("https://www.google.com/finance/quote/LKOH:MCX")
GAZP = update_ticker("https://www.google.com/finance/quote/GAZP:MCX")
SBER = update_ticker("https://www.google.com/finance/quote/SBER:MCX")
YNDX = update_ticker("https://www.google.com/finance/quote/YNDX:MCX")
PHOR = update_ticker("https://www.google.com/finance/quote/PHOR:MCX")
GMKN = update_ticker("https://www.google.com/finance/quote/GMKN:MCX")
ROSN = update_ticker("https://www.google.com/finance/quote/ROSN:MCX")
TCSG = update_ticker("https://www.google.com/finance/quote/TCSG:MCX")
VKCO = update_ticker("https://www.google.com/finance/quote/VKCO:MCX")
POLY = update_ticker("https://www.google.com/finance/quote/POLY:MCX")
AKRN = update_ticker("https://www.google.com/finance/quote/AKRN:MCX")
NVTK = update_ticker("https://www.google.com/finance/quote/NVTK:MCX")
AFLT = update_ticker("https://www.google.com/finance/quote/AFLT:MCX")
VTBR = update_ticker("https://www.google.com/finance/quote/VTBR:MCX")
MGNT = update_ticker("https://www.google.com/finance/quote/MGNT:MCX")


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/msc-market')
def rumarket():
    dt = datetime.datetime.now()
    return render_template("msk-market.html", time=dt.strftime('%d.%m.%Y %H:%M:%S'), LKOH=LKOH, GAZP=GAZP,
                           SBER=SBER, YNDX=YNDX, PHOR=PHOR, GMKN=GMKN, ROSN=ROSN, TCSG=TCSG, VKCO=VKCO,
                           POLY=POLY, AKRN=AKRN, NVTK=NVTK, AFLT=AFLT, VTBR=VTBR, MGNT=MGNT)

@app.route('/spb-market')
def market():
    return render_template("spb-market.html")




if __name__ == "__main__":
    app.run(debug=True)