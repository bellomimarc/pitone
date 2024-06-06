
from concurrent.futures import ThreadPoolExecutor
from time import sleep
from urllib.request import urlopen

from decorators import log_elapsed

def io1(sleep_time=1):
    sleep(sleep_time)
    return f"sleeping for {sleep_time} second"

def io2():
    try:
        with urlopen('http://httpbin.org/get') as response:
            return response.read()
    except Exception as e:
        pass

def io3():
    with open('log.txt', 'r') as f:
        return f.read()

@log_elapsed(unit="ms")
def ioBound():
    print(io1(0.3))
    print(io2())
    print(io3()[0:100])

@log_elapsed(unit="ms")
def ioBoundThreadFutures():
    with ThreadPoolExecutor(max_workers=None) as executor:
        f1 = executor.submit(io1, 0.3)
        f2 = executor.submit(io2)
        f3 = executor.submit(io3)

        print(f1.result())
        print(f2.result())
        print(f3.result()[0:100])

if __name__ == '__main__':
    ioBound()
    ioBoundThreadFutures()
