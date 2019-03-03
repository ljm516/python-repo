import re
import urllib.request

enter_url = 'https://www.csdn.net/'
header_name = 'User-Agent'
header_value = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
link_pattern = '(https?://[^\s";]+\.(\w|/)*)'


def get_links(url):
    opener = urllib.request.build_opener()
    header = (header_name, header_value)
    opener.addheaders = [header]

    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())
    link = re.compile(link_pattern).findall(data)

    link = set(link)
    return link


if __name__ == '__main__':
    link_list = get_links(enter_url)
    for link in link_list:
        print(link[0])

