from itertools import islice


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

for n in islice(nums, 3, 7):
    print(n)
