import json

yoldyz_token = '578689180:AAHOg6itFICVOOPoDG-cZ4JNWfImBZu_IRw'

translate_key = 'trnsl.1.1.20180330T192948Z.0e7154059c5810a7.997c509af45a23e81db12f0053ef803862542002'


def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
