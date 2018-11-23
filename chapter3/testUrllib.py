import urllib.parse
import urllib.request

if __name__ == "__main__":
    data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
    response = urllib.request.urlopen('http://httpbin.org/post', data=data)
    # response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
    request = urllib.request.Request('https://python.org')
    response1 = urllib.request.urlopen(request)
    print(str(response.read()))
    print(response1.read().decode('utf-8'))
