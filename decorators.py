def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

def log_elapsed(unit="s"):

    def log_elapsed_decorator(func):
        def inner():
            import datetime
            print("log_elapsed starts")
            now = datetime.datetime.now()
            func()
            print("log_elapsed ends")

            elapsed = datetime.datetime.now() - now
            case = {
                "ms": elapsed.microseconds / 1000,
                "s": elapsed.total_seconds(),
                "m": elapsed.total_seconds() / 60,
                "h": elapsed.total_seconds() / 3600
            }
            print(f"Elapsed time: {case[unit]} {unit}")
        return inner
    
    return log_elapsed_decorator

@log_elapsed(unit="ms")
@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()  