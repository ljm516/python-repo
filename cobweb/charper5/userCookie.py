import urllib.parse
import urllib.request
import http.cookiejar

url_1 = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LX15B'
url_2 = 'http://bbs.chinaunix.net/'

header_name = 'User-Agent'
header_value = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
               'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
post_data = urllib.parse.urlencode({'username': 'weisuen', 'password': 'aA123456'}).encode('utf-8')


def no_cookie():
    req_1 = urllib.request.Request(url_1, post_data)
    req_1.add_header(header_name, header_value)
    data_1 = urllib.request.urlopen(req_1).read()

    with open('D:\\lijiangming\\cobweb\\charpter5\\no_cookie.html', 'wb') as f_handler:
        f_handler.write(data_1)

    req_2 = urllib.request.Request(url_2, post_data)
    req_2.add_header(header_name, header_value)

    data_2 = urllib.request.urlopen(req_2).read()
    with open('D:\\lijiangming\\cobweb\\charpter5\\no_cookie_2.html', 'wb') as f_handler:
        f_handler.write(data_2)


def has_cookie():
    req_1 = urllib.request.Request(url_1, post_data)
    req_1.add_header(header_name, header_value)
    cjar = http.cookiejar.CookieJar()  # 创建 CookieJar 对象

    #  使用 HTTPCookieProcessor 创建 cookie 处理器，并以其为参数构建 opener 对象
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
    urllib.request.install_opener(opener)
    file = opener.open(req_1)
    data_1 = file.read()
    with open('D:\\lijiangming\\cobweb\\charpter5\\has_cookie.html', 'wb') as f_handler:
        f_handler.write(data_1)

    data_2 = urllib.request.urlopen(url_2).read()
    with open('D:\\lijiangming\\cobweb\\charpter5\\has_cookie_2.html', 'wb') as f_handler:
        f_handler.write(data_2)


if __name__ == '__main__':
    has_cookie()
