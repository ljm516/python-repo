import urllib.request
import re
import time
import urllib.error

header_name = 'User-Agent'
header_value = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
               'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
headers = (header_name, header_value)
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
article_url_list = []
input_data = ''


def user_proxy(proxy_add, url):
    try:
        proxy = urllib.request.ProxyHandler({'http': proxy_add})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        urllib.request.install_opener(opener)
        data = urllib.request.urlopen(url).read().encode('utf-8')
        return data
    except urllib.request.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print('exception: ', str(e))
        time.sleep(10)


def get_article_url_list(key, page_start, page_end, proxy):
    try:
        page = page_start
        keycode = urllib.request.quote(key)
        pagecode = urllib.request.quote('&page=')

        for page in range(page_start, page_end + 1):
            url = 'http://weixin.sogou.com/weixin?type=2&query=&' + keycode + pagecode + str(page)
            # data = user_proxy(proxy, url)
            data = urllib.request.urlopen(url).read()
            url_list_pattern = '<div class="txt-box">.*?(http://.*?)"'
            article_url_list.append(re.compile(url_list_pattern, re.S).findall(data))

        print('共获取到 ', str(len(article_url_list)) + '页')

        return article_url_list

    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print('exception: ' + str(e))
        time.sleep(10)


def get_content(article_url_list, proxy):
    i = 0

    for i in range(0, len(article_url_list)):
        for j in range(0, len(article_url_list[i])):
            try:
                url = article_url_list[i][j]
                url = url.replace('amp;', '')
                # data = user_proxy(proxy, url)
                data = urllib.request.urlopen(url).read()
                title_pattern = '<title>(.*?)</title>'
                content_pattern = 'id="js_content">(.*?)id="js_sg_bar"'
                title = re.compile(title_pattern).findall(data)
                content = re.compile(content_pattern, re.S).findall(data)
                this_title = 'no query'
                this_content = 'no query'
                if title != []:
                    this_title = title[0]
                if content != []:
                    this_content = content[0]
                data_all = "标题: " + this_title + '\n内容: ' + this_content + '\n'
                input_data = input_data + data_all
                print('第' + str(i) + '个网页第' + str(j) + '次处理')
            except urllib.request.URLError as e:
                if hasattr(e, 'code'):
                    print(e.code)
                if hasattr(e, 'reason'):
                    print(e.reason)
                time.sleep(10)
            except Exception as e:
                print('exception: ' + str(e))
                time.sleep(10)

    with open('D:\\lijiangming\\cobweb\\chartper6\\wechat_search.html', 'wb') as fhandler:
        fhandler.write(input_data)


if __name__ == '__main__':
    key = 'python'
    proxy = '123.206.132.106:8888'
    page_start = 1
    page_end = 2
    url_list = get_article_url_list(key, page_start, page_end, proxy)
    get_content(url_list, proxy)

