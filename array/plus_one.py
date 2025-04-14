input = [1,2,3]
# input = [1,9]
input = [9]

def plus_one(input):
    # we loop over every item in array in reverse order
    # we increment last item by one
    # then we check it, if it's 10
    # we change it to 0 and continue 
    # if not 10, break loop and exit
    
    # if we went throught the entire loop
    # that means last item also was 10
    # which means we need to append [1] to the original array
    for i in range(len(input) -1, -1, -1):
        input[i] += 1
        if input[i] == 10:
            input[i] = 0
        else:
            return input
        return [1] + input

print(plus_one(input))


