#                         0  1  2  3  4  5
a = [1, 2, 3, 4, 5, 4]
a = [2, 2, 1]
slow = a[0]
fast = a[0]

# s 2
# f 3

# s3
# f5

# s4
# f5
while True:
    slow = a[slow]
    print(f"{slow=}")
    fast = a[a[fast]]
    print(f"{fast=}")
    if slow == fast:
        break
slow = a[0]
while slow != fast:
    slow = a[slow]
    fast = a[fast]
print(slow)
