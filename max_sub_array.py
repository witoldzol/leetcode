nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maximum = 0
current = 0
for idx, n in enumerate(nums):
    if current + n < 0:
        # reset counter / index when we hit zero
        maximum = 0
        current = 0
        continue
    # otherwise keep going and keep adding, updating max if you hit it
    current += n
    if current > maximum:
        maximum = current
print(maximum)
maximum = 0
current = 0
for idx, n in enumerate(nums):
    if current + n < 0:
        # reset counter / index when we hit zero
        maximum = 0
        current = 0
        continue
    # otherwise keep going and keep adding, updating max if you hit it
    current += n
    if current > maximum:
        maximum = current
print(maximum)
