import urllib.request
import re

header_name = 'User-Agent'
header_value = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
               'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'


def get_content(url, page):
    
    opener = urllib.request.build_opener()
    headers = (header_name, header_value)
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(url).read().decode('utf-8')
    
    # with open('qiushibaike_'.join(str(page)).join('.html'), 'w', encoding='utf-8' ) as html:
    #     html.write(data)

    # user_pattern = '<a target="_blank">'
    user_pattern = '<h2>(.*?)</h2>'
    content_pattern = '<div class="content">(.*?)</div>'
    
    user_list = re.compile(user_pattern, re.S).findall(data)
    print('user_list {userList}'.format(userList=user_list))

    content_list = re.compile(content_pattern, re.S).findall(data)
    print('content_list {contentList}'.format(contentList=content_list))
    
    x = 1
    for content in content_list:
        content = content.replace('\n', '')
        name = 'content' + str(x)
        exec(name + '=content')
        x += 1
    y = 1

    print('----------------------------------------------------------------------------------------------------')

    for user in user_list:
        name = 'content' + str(y)
        print('用户' + str(page) + str(y) + '是: ' + user)
        print('内容是: ')
        exec("print(" + name + ")")
        print('\n')
        y += 1


if __name__ == '__main__':
    for i in range(1, 3):
        url = 'http://www.qiushibaike.com/8hr/page/' + str(i)
        print('url is {url}'.format(url=url))
        get_content(url, i)
