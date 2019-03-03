import urllib.error

try:
    import urllib.request
    urllib.request.urlopen('http://blog.csdn.net.ccc')
except urllib.error.HTTPError as e:
    print('HTTPError')
    print(e.code)
    print(e.reason)
except urllib.error.URLError as e:
    print('URLError')
    print(e.reason)
