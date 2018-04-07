from flask import Flask
from flask import request
from flask import jsonify
import requests
import re

from flask_sslify import SSLify

from misc import yoldyz_token, write_json
from translate import to_translate

app = Flask(__name__)
sslify = SSLify(app)


def query(method):
    return 'https://api.telegram.org/bot{token}/{method}'.format(
        token=yoldyz_token,
        method=method
    )


def set_message(chat_id, text='hello', reply_to_message_id=-1):
    url = query('sendMessage')
    answer = {'chat_id': chat_id,
              'text': text}
    if reply_to_message_id != -1:
        answer['reply_to_message_id'] = reply_to_message_id
    r = requests.post(url, json=answer)
    return r.json()


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        r = request.get_json()
        message_json = r['message']
        chat_id = message_json['chat']['id']
        message = message_json['text']
        reply_to_message_id = int(message_json['message_id'])
        print(type(reply_to_message_id))
        print(message)
        write_json(r)

        seps = set(['по татарски ', 'тат '])
        answers = {'wtf': 'бу сүз шундый',
                   'many': 'ничек күп сүзләр'}

        for sep in seps:
            if sep in message:
                text = re.split(sep, message)

                translation = to_translate(text)
                set_message(chat_id, text=translation, reply_to_message_id=reply_to_message_id)

        # write_json(r)
        return jsonify(r)
    return '<h1>Bot welcomes you</h1>'


if __name__ == '__main__':
    app.run()
