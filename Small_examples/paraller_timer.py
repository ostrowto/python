#paraller_timer.py

from timeit import default_timer as timer

start = timer()
a = [i*i for i in range(1_000_000)]
end = timer()
print("Timer 1: ", end-start)

start = timer()
a = []
for i in range(1_000_000):
    a.append(i*i)
end = timer()
print("Timer 2: ", end-start)
