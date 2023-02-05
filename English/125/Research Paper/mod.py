from time import perf_counter

t = perf_counter()
n = 5000047
for i in range(1,n):
    x = (3**i)  % n
    if x == 1:
        print(i)
        print(perf_counter()-t)
        break