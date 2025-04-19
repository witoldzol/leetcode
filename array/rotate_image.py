import sys
from typing import List
import math
# input = [[1,2,3,4],
#          [4,5,6,8],
#          [7,8,9,8],
#          [7,8,9,8]
#         ]
# input = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# out = [[7,4,1],[8,5,2],[9,6,3]]
# input = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# out= [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
input = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
out= [[13,9,5,1],
      [14,10,6,2],
      [15,11,7,3],
      [16,12,8,4]]
class Solution:
    def rotate_layer(self, start,end, matrix):
        for idx,i in enumerate(range(start,end)):
            print(f'ITERATION : {i}, LAYER start {start}, end: {end}')
            temp = matrix[i][end] #3
            print(f'L->R replacing {matrix[i][end]} : [{i}][{end}] with {matrix[start][i]} - [{start}][{i}]')
            matrix[i][end] = matrix[start][i]
            # go down
            temp2 = matrix[end][end-idx]
            print(f'GO DOWN replacing {matrix[end][end-idx]} [{end}][{end-idx}] with {temp} [{i}][{end}]')
            matrix[end][end-idx] = temp
            temp = temp2
            # left right
            temp2 = matrix[end - idx][start] #7
            print(f'L -> R replacing {matrix[end - idx][start]} with {temp}')
            matrix[end - idx][start] = temp
            temp = temp2
            # go up
            print(f'GO UP replacing {matrix[start][i]} with {temp}')
            matrix[start][i] = temp
            print(f'==========')


    def rotate(self, matrix: List[List[int]]) -> None:
        start = 0
        end = len(matrix) - 1
        while start < end:
            self.rotate_layer(start, end, matrix)
            start += 1
            end -= 1
        for x in matrix:
            print(x)
        return matrix
            
actual = Solution().rotate(input)
assert actual == out, f"{actual} should be {out}"
print('EXPECTED')
for x in  out:
    print(x)
