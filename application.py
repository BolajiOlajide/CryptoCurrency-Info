from flask import Flask, render_template
import requests

app = Flask(__name__)

# app.config['DEBUG'] = True
# Uncomment the line above if you want to run the application in dev mode
# or if you need the server to auto-restart if you make changes


@app.route('/')
def index():
    cryptos = requests.get('https://api.coinmarketcap.com/v1/ticker/?limit=10')
    return render_template('index.html', cryptos=cryptos.json())


if __name__ == '__main__':
    app.run()
