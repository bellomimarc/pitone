import threading
import queue
from time import sleep
from typing import MutableSequence

q = queue.Queue()

def worker():
    while True:
        item = q.get()
        print(f'Working on {item}')
        sleep(0.5)
        print(f'Finished {item}')
        q.task_done()

# Turn-on the worker thread.
workers: MutableSequence[threading.Thread] = []
for i in range(5):
    t = threading.Thread(target=worker, daemon=True)
    workers.append(t)
    t.start()

# Send thirty task requests to the worker.
for item in range(20):
    q.put(item)

# Block until all tasks are done.
q.join()
print('All work completed')