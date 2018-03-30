import requests

from misc import yoldyz_token


def point(event, context):
    print(event)
    print('hello')

'''
def start_request():
    url = 'https://api.telegram.org/bot{token}/{method}'.format(
        token=yoldyz_token,
        method='setWebhook'
    )
    data = {
        'url': 'https://c360b099.ngrok.io'
    }
    r = requests.post(url, data=data)
    print(r.json())

if __name__ == '__main__':
    start_request()
'''