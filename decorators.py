import time
from tracemalloc import start


def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

def log_elapsed(unit="s"):

    def log_elapsed_decorator(func):
        def inner():
            # print("log_elapsed starts")
            start = time.time()
            func()
            # print("log_elapsed ends")

            end = time.time()
            elapsed = end - start
            case = {
                "s": elapsed,
                "ms": elapsed * 1000,
                "us": elapsed * 1000000
            }
            print(f"Elapsed time {func.__name__}: {case[unit]} {unit}")
        return inner
    
    return log_elapsed_decorator

@log_elapsed(unit="ms")
@make_pretty
def ordinary():
    print("I am ordinary")

if __name__ == '__main__':
    ordinary()