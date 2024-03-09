nums = [3, 2, 4]
nums = [3, 3]


def two_sum(nums, target):
    for ix, x in enumerate(nums):
        diff = target - x
        print(f"diff for x = {x} is {diff}")
        for iy, y in enumerate(nums):
            if ix == iy:
                continue
            if y == diff:
                return ix, iy


def two(nums, target):
    diffs = {}
    for ix, x in enumerate(nums):
        if x in diffs and diffs[x] != ix:
            return diffs[x], ix
        diff = target - x
        diffs[diff] = ix


print(f"solution = {two_sum(nums, 6)}")
print(f"solution = {two(nums, 6)}")
