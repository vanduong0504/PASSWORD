import requests
import hashlib


def read_txt(file):
    with open(file, mode='r') as file:
        output = file.read().splitlines()
    return output


def convert_SHA1(string):
    SHA1 = hashlib.sha1(string.encode()).hexdigest().upper()
    return SHA1[0:5], SHA1[5:]


def get_response(char):
    url = 'https://api.pwnedpasswords.com/range/' + char
    request = requests.get(url)
    return [line.split(":") for line in request.text.splitlines()]


def check(password_, response_):
    for item in response_:
        if password_ == item[0]:
            return item[1]
    return 0


if __name__ == '__main__':
    passwords = read_txt("input.txt")
    for password in passwords:
        first, last = convert_SHA1(password)
        response = get_response(first)
        time = check(last, response)
        pw = f'Your password is {len(password)*"*"}.'
        if time:
            print(f'{pw} Found {time} times on the Internet!!!')
        else:
            print(f'{pw} You can use your password on the Internet <3')
