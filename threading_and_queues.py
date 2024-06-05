from functools import lru_cache
import sys
import threading
import queue
from time import sleep
from token import NUMBER
from typing import MutableSequence
from urllib.request import urlopen

from decorators import log_elapsed

NUMBER_OF_WORKERS = int(sys.argv[1]) if len(sys.argv) > 1 else 5
NUMBER_OF_TASKS = int(sys.argv[2]) if len(sys.argv) > 2 else 20

q = queue.Queue()

def httpbin():
    try:
        with urlopen('http://httpbin.org/get') as response:
            pass
    except Exception as e:
        pass

def ioWorker():
    while True:
        item = q.get()
        # print(f'Working on {item}')
        httpbin()
        # print(f'Finished {item}')
        q.task_done()

# @lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def cpuWorker():
    while True:
        item = q.get()
        # print(f'Working on {item}')
        fibonacci(30)
        # print(f'Finished {item}')
        q.task_done()

@log_elapsed(unit="ms")
def ioBound():
    # Turn-on the worker thread on worker with IO bound tasks
    ioWorkers: MutableSequence[threading.Thread] = []
    for i in range(NUMBER_OF_WORKERS):
        t = threading.Thread(target=ioWorker, daemon=True)
        ioWorkers.append(t)
        t.start()

    # Send thirty task requests to the worker.
    for item in range(NUMBER_OF_TASKS):
        q.put(item)

    # Block until all tasks are done.
    q.join()

@log_elapsed(unit="ms")
def cpuBound():
    # Turn-on the worker thread on worker with CPU bound tasks
    cpuWorkers: MutableSequence[threading.Thread] = []
    for i in range(NUMBER_OF_WORKERS):
        t = threading.Thread(target=cpuWorker, daemon=True)
        cpuWorkers.append(t)
        t.start()

    # Send thirty task requests to the worker.
    for item in range(NUMBER_OF_TASKS):
        q.put(item)

    # Block 
    # until all tasks are done.
    q.join()

if __name__ == '__main__':
    ioBound()
    cpuBound()