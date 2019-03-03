import requests
from json import dumps

head = {
    'Accept': 'application/json',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsImlhdCI6MTQ5NzU4MDY5NywiZXhwIjoxNTEzMTMyNjk3fQ.eyJpZCI6MjB9.uo8JdyzBBQ-oGxzMyoiFDlycWk-fqagZLVgwrwqTSBM',
    'Content-Type': 'application/json',
    'Host': 'api.wayknew.com',
    'Referer': 'https://wayknew.com/articles/535/edit',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}


def write_to_wayknew():
    title = 'yolar 线上API文档'
    url = 'https://api.wayknew.com/api/articles/535'
    request_data = {'title': title, 'content': 'test send patch ......', 'html_content': '<p>test send patch ...... .</p>'}
    r = requests.patch(url, dumps(request_data), headers=head)

    if r.status_code != 200:
        print(r.text)
        exit(0)

    print(r.text)


if __name__ == '__main__':
    write_to_wayknew()
