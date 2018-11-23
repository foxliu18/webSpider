from urllib import request, error

if __name__ == '__main__':

    try:
        response1 = request.urlopen('https://cuiqingcai.com/index.htm')
    except error.HTTPError as e:
        print(e.reason, e.code, e.headers, sep='\n')
    except error.URLError as e:
        print(e.reason)
    else:
        print('Request Successfully')

