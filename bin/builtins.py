#map

# r = map(func, list)
# r = filter(func, list)

from functools import reduce

r4 = map(lambda p: p-10, [100, 200, 300])

print(list(r4))



L = [(lambda i: i*i)(a) for a in range(10)]