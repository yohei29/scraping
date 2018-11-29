import time
import requests
from retrying import retry

ERROR_CODE = (408,500,502,503,504)


def main():

    res = fetch('http://httpbin.org/status/202,404,503')

    if 200 <= res.status_code <300:
        print('access')
    else:
        print('ERROR')

@retry(stop_max_attempt_number=3,
       wait_exponential_multiplier=1000)
def fetch(url):
    print('Retrieving {0}...'.format(url))
    res = requests.get(url)
    print('Status: {0}'.format(res.status_code))

    if res.status_code not in ERROR_CODE:
        return res

    print('Status error. plz wait...')
    raise Exception('Temporary Error: {0}'.format(res.status_code))

if __name__ == '__main__':
    main()