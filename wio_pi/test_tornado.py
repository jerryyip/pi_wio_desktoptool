# coding:utf-8

from tornado.httpclient import HTTPClient
from time import sleep
from urllib2 import urlopen

WIO_URL = "https://cn.wio.seeed.io/v1/node/GroveUltraRangerD0/range_in_cm\?access_token\=7093a8f74d427dc4d2bf4d732ed74183"


def synchronous_fetch(url):
    http_client = HTTPClient()
    response = http_client.fetch(url)
    return response.body


if __name__ == '__main__':
    while True:
    	sleep(0.1)
        # print(synchronous_fetch(WIO_URL))
        html = urlopen(WIO_URL)
        print(html.read())
