import requests

if __name__ == '__main__':
    s = requests.Session()
    s.get('http://httpbin.org/cookies/set/number/123456789')
    r = s.get('http://httpbin.org/cookies')
    print(r.text)
