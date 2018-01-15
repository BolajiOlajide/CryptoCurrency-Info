from flask import Flask, render_template
import requests

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    cryptos = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=10')
    cryptos = cryptos.json()
    return render_template('index.html', cryptos=cryptos)


if __name__ == '__main__':
    app.run()
