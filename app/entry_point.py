from flask import Flask
from flask import request
from flask import jsonify
import requests
import re

from flask_sslify import SSLify

from misc import yoldyz_token, write_json

app = Flask(__name__)
sslify = SSLify(app)


def query(method):
    return 'https://api.telegram.org/bot{token}/{method}'.format(
        token=yoldyz_token,
        method=method
    )


def set_message(chat_id, text='hello'):
    url = query('sendMessage')
    answer = {'chat_id': chat_id,
              'text': text}
    r = requests.post(url, json=answer)
    return r.json()


def parse_test(text):
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()
    return crypto[1:]


def get_price(crypto):
    url = 'https://api.coinmarketcap.com/v1/ticker/{}/'.format(crypto)
    r = requests.get(url).json()
    price = r[-1]['price_usd']
    return price


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        message = r['message']['text']

        pattern = r'/\w+'

        if re.search(pattern, message):
            price = get_price(parse_test(message))
            set_message(chat_id, text=price)

        # write_json(r)
        return jsonify(r)
    return '<h1>Bot welcomes you</h1>'


if __name__ == '__main__':
    # start_request()
    # entry_point()
    app.run()
