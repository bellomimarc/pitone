import datetime
import json
import time
from urllib.request import urlopen, Request
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()             # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())  

postRequest = Request('http://httpbin.org/post', data=b'some data', method='POST')

beforerequest = time.time()
with urlopen(postRequest) as response:
    print("elapsed request time: ", (time.time() - beforerequest) * 1000, "ms")
    afterrequest = datetime.datetime.now()
    r = json.load(response)
    print("elapsed json.load time: ", (datetime.datetime.now() - afterrequest).microseconds / 1000, "ms")
    
    # print all key-value pairs in the response
    for key, value in r.items():
        print(key, ":", value)

    # print the value of the key 'data'
    print("form>>>>>>>", r['form'])

    