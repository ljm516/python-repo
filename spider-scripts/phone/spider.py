import requests
import json


def crawling(key):
    print("current key={}".format(key))
    for i in range(2):
        request_url = "http://mobsec-dianhua.baidu.com/dianhua_api/open/location?tel=" + str(key)
        try:
            rsp_content = requests.get(request_url, timeout=5).content
            json_obj = json.loads(rsp_content)

            data_json = json_obj['response']
            rsp_json = json_obj['responseHeader']
            if rsp_json['status'] != 200:
                print("response not success, i={}".format(i))
            else:
                if data_json[str(key)] is not None:
                    detail_json = data_json[str(key)]['detail']
                    operator = detail_json['operator']
                    print("operator={}".format(operator))
                    return operator

                break
        except requests.exceptions.RequestException as e:
            print("key={}timeout".format(key))
            break
