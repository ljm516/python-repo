import re
import urllib.request

cache_dict = "D:\\lijiangming\\cobweb\\chartper6\\jd_images\\"


def craw_jd_images(url, page):
    html_1 = urllib.request.urlopen(url).read()
    html_1 = str(html_1)
    pattern_1 = '<div id="plist".+? <div class="page clearfix">'
    result_1 = re.compile(pattern_1).findall(html_1)
    result_1 = result_1[0]
    pattern_2 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    image_list = re.compile(pattern_2).findall(result_1)

    x = 1
    for image_url in image_list:
        image_name = cache_dict + str(page) + str(x) + '.jpg'
        image_url = 'http://' + image_url
        try:
            urllib.request.urlretrieve(image_url, filename=image_name)
        except urllib.error.URLError as e:
            if hasattr(e, 'code'):
                x += 1
            if hasattr(e, 'reason'):
                x += 1


if __name__ == '__main__':

    for i in range(1, 10):
        url = 'https://list.jd.com/list.html?cat=9987,653,655&page=' + str(i)
        craw_jd_images(url, i)
