from urllib.parse import urlparse

if __name__ == '__main__':
    result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
    print(type(result), result)
