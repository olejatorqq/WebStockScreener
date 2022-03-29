from flask import Flask, render_template, url_for, request, redirect
import datetime
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


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
    return render_template("msk-market.html", time=dt.strftime('%d.%m.%Y %H:%M:%S'))

@app.route('/spb-market')
def market():
    return render_template("spb-market.html")




if __name__ == "__main__":
    app.run(debug=True)