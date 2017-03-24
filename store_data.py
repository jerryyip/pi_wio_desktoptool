import csv
from urllib2 import Request, urlopen, URLError, HTTPError
import json
import time


WIO_TOKEN = "7093a8f74d427dc4d2bf4d732ed74183"
url = "https://cn.wio.seeed.io/v1/node/GroveUltraRangerD0/range_in_cm?access_token=%s" % WIO_TOKEN
request = Request(url)

def storeData(desk_state):
    try:
        with open("data.csv",'a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow((time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),desk_state))
    except Exception as e:
        print(e)


def getData():
    try:
        response = urlopen(request)
        data = response.read()
        result = json.loads(data)

        if result["range_cm"]>20.0:
            # No man on the desk, return 1; else return 2
            return 1
        else:
            return 2
    except Exception as e:
        # When wio is offline, return 0
        return 0


def main():
    while True:
        storeData(getData())
        time.sleep(2)

if __name__ == '__main__':
    main()