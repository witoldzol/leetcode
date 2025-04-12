# input = [1,2,3]
# expected = [1,2,4]
# input = [1,9]
# expected = [2,0]
input = [9]
expected = [1,0]

def plus_one(input):
    for i in range(len(input)):
        idx = len(input) - 1 - i
        input[idx] += 1
        if input[idx] == 10:
            input[idx]= 0
        else:
            return input
    return [1] + input

print(input)
print(plus_one(input))

