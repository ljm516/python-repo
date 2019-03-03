from urllib.parse import urlencode
from urllib.request import Request
from urllib.request import urlopen


def http_get():
    response = urlopen('http://www.baidu.com')
    html = response.read()
    print(html)


def http_post():
    url = 'https://mail.qq.com/cgi-bin/login'
    post_data = {"username": '******', 'password': '******'}
    data = urlencode(post_data).encode('utf-8')
    req = Request(url, data)
    response = urlopen(req)
    html = response.read()
    print(html)
    with open('mail_qq_com_login.html', 'wb') as out_file:
        out_file.write(html)


if __name__ == '__main__':
    http_post()
