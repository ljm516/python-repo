from json import dumps

import requests

d = {'yolar': 535, 'galaxy': 536, 'solar': 551, 'swordkeeper': 552, 'civilization': 553, 'CurvatureDrive': 554,
     'singer': 555, 'hdfragments': 556, 'evans': 557, 'dagon': 558, 'di-foil': 559, 'dimension': 560, 'farmer': 562,
     'hibernation': 564, 'huformation': 565, 'mentalseal': 566, 'midas': 567, 'momentum': 568, 'owl': 569,
     'shooter': 570, 'sophon': 571, 'bye': 573, 'cms': 575, 'nsk': 576, 'painter': 577, 'redcoast': 578,
     'scientificboundary': 579, 'wall-breaker': 580}

head = {
    'Accept': 'application/json',
    'Authorization': 'eyJhbGciOiJIUzI1NiIsImlhdCI6MTQ5NzU4MDY5NywiZXhwIjoxNTEzMTMyNjk3fQ.eyJpZCI6MjB9.uo8JdyzBBQ-oGxzMyoiFDlycWk-fqagZLVgwrwqTSBM',
    'Content-Type': 'application/json',
    'Host': 'api.wayknew.com',
    'Referer': 'https://wayknew.com/articles/535/edit',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}


def write_to_wayknew(repo_name, str_doc):
    if repo_name not in d.keys():
        print('article not in wayknew, please create a null article in wayknew!')
        exit(-1)
    title = repo_name + ' 线上API文档'
    url = 'https://api.wayknew.com/api/articles/' + str(d[repo_name])
    html_content = '<p>' + str_doc + '</p>'
    request_data = {'title': title, 'content': str_doc, 'html_content': html_content}
    rsp = requests.patch(url, dumps(request_data), headers=head)

    if rsp.status_code != 200:
        print(rsp.text)
        exit(rsp.status_code)

    print(repo_name + ' api write to wayknew success')
