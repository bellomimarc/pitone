from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from multiprocessing import Pool
import os
import sys
import threading
import queue
from typing import MutableSequence
from urllib.request import urlopen

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from decorators import log_elapsed

NUMBER_OF_WORKERS = int(sys.argv[1]) if len(sys.argv) > 1 else 5
NUMBER_OF_TASKS = int(sys.argv[2]) if len(sys.argv) > 2 else 20

print(f"Number of workers: {NUMBER_OF_WORKERS}")
print(f"Number of tasks: {NUMBER_OF_TASKS}")

q = queue.Queue()

def httpbin(item: int = None):
    try:
        with urlopen('http://httpbin.org/get') as _:
            pass
    except Exception as _:
        pass

def ioWorker():
    while True:
        _ = q.get()
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
        _ = q.get()
        # print(f'Working on {item}')
        fibonacci(30)
        # print(f'Finished {item}')
        q.task_done()

@log_elapsed(unit="ms")
def ioBoundThread():
    # Turn-on the worker thread on worker with IO bound tasks
    ioWorkers: MutableSequence[threading.Thread] = []
    for i in range(NUMBER_OF_WORKERS):
        t = threading.Thread(target=ioWorker, daemon=True, name=f"worker-{i}")
        ioWorkers.append(t)
        t.start()

    # Send thirty task requests to the worker.
    for item in range(NUMBER_OF_TASKS):
        q.put(item)

    # Block until all tasks are done.
    q.join()

@log_elapsed(unit="ms")
def cpuBoundThread():
    # Turn-on the worker thread on worker with CPU bound tasks
    cpuWorkers: MutableSequence[threading.Thread] = []
    for i in range(NUMBER_OF_WORKERS):
        t = threading.Thread(target=cpuWorker, daemon=True, name=f"worker-{i}")
        cpuWorkers.append(t)
        t.start()

    # Send thirty task requests to the worker.
    for item in range(NUMBER_OF_TASKS):
        q.put(item)

    # Block 
    # until all tasks are done.
    q.join()

@log_elapsed(unit="ms")
def cpuBound():
    for i in range(NUMBER_OF_TASKS):
        fibonacci(30)

@log_elapsed(unit="ms")
def ioBound():
    for i in range(NUMBER_OF_TASKS):
        httpbin()

@log_elapsed(unit="ms")
def ioBoundThreadFutures():
    with ThreadPoolExecutor(max_workers=NUMBER_OF_WORKERS) as executor:
        for i in range(NUMBER_OF_TASKS):
            executor.submit(httpbin)

@log_elapsed(unit="ms")
def cpuBoundThreadFutures():
    with ThreadPoolExecutor(max_workers=NUMBER_OF_WORKERS) as executor:
        for i in range(NUMBER_OF_TASKS):
            executor.submit(fibonacci, 30)

@log_elapsed(unit="ms")
def ioBoundProcessFutures():
    with ProcessPoolExecutor(max_workers=NUMBER_OF_WORKERS) as executor:
        for i in range(NUMBER_OF_TASKS):
            executor.submit(httpbin)

@log_elapsed(unit="ms")
def cpuBoundProcessFutures():
    with ProcessPoolExecutor(max_workers=NUMBER_OF_WORKERS) as executor:
        for i in range(NUMBER_OF_TASKS):
            executor.submit(fibonacci, 30)

@log_elapsed(unit="ms")
def cpuBoundPool():
    with Pool(processes=NUMBER_OF_WORKERS) as pool:
        pool.map(fibonacci, [30] * NUMBER_OF_TASKS)

@log_elapsed(unit="ms")
def ioBoundPool():
    with Pool(processes=NUMBER_OF_WORKERS) as pool:
        pool.map(httpbin, [None] * NUMBER_OF_TASKS)

if __name__ == '__main__':
    ioBound()
    ioBoundThread()
    ioBoundThreadFutures()
    ioBoundProcessFutures()
    ioBoundPool()
    cpuBound()
    cpuBoundThread()
    cpuBoundThreadFutures()
    cpuBoundProcessFutures()
    cpuBoundPool()