import requests
import re

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0(Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36'
                      '(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
    }
    r = requests.get('https://www.zhihu.com/explore', headers=headers)
    pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
    titles = re.findall(pattern, r.text)
    # print(titles, '\n')

    r_image = requests.get("https://github.com/favicon.ico")
    # with open('favicon.ico', 'wb') as f:
    #     f.write(r.content)

    r_cookies = requests.get("https://www.baidu.com")
    print(r_cookies.cookies)
    for key, value in r.cookies.items():
        print(key + '=' + value)
