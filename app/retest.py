import re


def main():
    pattern = ''
    text = 'как будет по татарски привет'
    text = 'asd '

    sep = 'по татарски '
    space = ' '

    if space in text.strip():
        result = re.split(space, text)
        print('many')
    else:
        print('one')


if __name__ == '__main__':
    main()
