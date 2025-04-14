nums = [2,7,11,15]
target = 9
output = [0,1]

def two_sum(nums, target):
    # save here t - n ( 15, -6 )
    m = {}
    for i, n in enumerate(nums):
        if n in m:
            return [i, m[n]]
        else:
            diff = target - n
            m[diff] = i
print(two_sum(nums,target))
