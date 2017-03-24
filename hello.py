from flask import Flask
from urllib2 import Request, urlopen, URLError, HTTPError
import json
import time


WIO_TOKEN = "7093a8f74d427dc4d2bf4d732ed74183"

url = "https://cn.wio.seeed.io/v1/node/GroveUltraRangerD0/range_in_cm?access_token=%s" % WIO_TOKEN
request = Request(url)

def foo():
    try:
        response = urlopen(request)
        data = response.read()
        result = json.loads(data)

        if result["range_cm"]:
            return result["range_cm"]
    except Exception as e:
        return e



app = Flask(__name__)

@app.route('/')
def hello_world():
    while True:
        a = foo()
        return ("%s cm" % a,)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')