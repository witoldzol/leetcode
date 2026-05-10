nums = [2, 7, 11, 15]
target = 9
d = {}
for idx, n in enumerate(nums):
    if n in d:
        print(sorted([d[n], idx]))
        break
    diff = target - n
    d[diff] = idx
