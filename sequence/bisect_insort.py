import bisect
import random

SIZE = 7

random.seed(1729) # set init random seed.

my_list = []

for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    # bisect.bisect_left(my_list, new_item)
    print('%2d -> ' % new_item, my_list)

l = [random.randint(0, 100) for _ in range(100)]
print(l)
print(l.clear())