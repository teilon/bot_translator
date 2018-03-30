import requests
import json

from misc import yoldyz_token


# def start_request():
#     url = 'https://api.telegram.org/bot{token}/{method}'.format(
#         token=yoldyz_token,
#         method='setWebhook'
#     )
#     data = {
#         'url': 'https://c360b099.ngrok.io'
#     }
#     r = requests.post(url, data=data)
#     print(r.json())

def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def query(method):
    return 'https://api.telegram.org/bot{token}/{method}'.format(
        token=yoldyz_token,
        method=method
    )


def get_updates():
    url = query('getUpdates')
    r = requests.get(url)
    # write_json(r.json())
    return r.json()


def set_message(chat_id, text='hello'):
    url = query('sendMessage')
    answer = {'chat_id': chat_id,
              'text': text}
    r = requests.post(url, json=answer)
    return r.json()


def entry_point():
    r = get_updates()
    chat_id = r['result'][-1]['message']['chat']['id']
    set_message(chat_id)


if __name__ == '__main__':
    # start_request()
    entry_point()
