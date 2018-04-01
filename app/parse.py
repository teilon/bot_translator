import requests
from misc import write_json
import re


def parse_test(text):
    pattern = r'/\w+'
    crypto = re.search(pattern, text).group()
    return crypto[1:]


def get_price(crypto):
    url = 'https://api.coinmarketcap.com/v1/ticker/{}/'.format(crypto)
    r = requests.get(url).json()
    price = r[-1]['price_usd']
    return price


def main():
    # print(get_price())
    print(get_price(parse_test('сколько стоит биткоин /ethereum?')))


if __name__ == '__main__':
    main()
