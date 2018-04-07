import requests

from misc import translate_key, write_json


def lang_test(lang_key='en'):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/getLangs'
    params = {'key': translate_key,
              'lang': lang_key}
    r = requests.post(url, params=params)
    return r.json()


def get_translate(text):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {'key': translate_key,
              'text': text,
              'lang': 'ru-tt'}
    r = requests.post(url, params=params)
    return r.json()


def to_translate(text):
    r = get_translate(text)
    write_json(r, 'translate.json')
    if r['code'] == 200:
        return r['text'][1]
    return ''


def test():
    print(translate_key)


def main():
    # test()
    r = to_translate('Добрый утро')

    # r = lang_test()
    write_json(r, 'translate.json')
    print(r)

if __name__ == '__main__':
    main()
