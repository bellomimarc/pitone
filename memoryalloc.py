# importing the module
import tracemalloc

# code or function for which memory
# has to be monitored
def app():
    lt = []
    for i in range(0, 10000000):
        lt.append(i)

# starting the monitoring
tracemalloc.start()

# function call
app()

# displaying the memory
print(tracemalloc.get_traced_memory()[1] / 10**6, "MB")

# stopping the library
tracemalloc.stop()