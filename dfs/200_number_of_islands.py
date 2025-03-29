from collections import deque
from typing import List
grid_1= [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid_3= [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
class Solution:
    def island_exists(self, i: int, k: int, ISLANDS) -> bool:
        return (i,k) in ISLANDS

    def explore_island(self, i: int, k: int, grid: list[list[str]], ISLANDS) -> None:
        queue = deque()
        visited  = set()
        if (i,k) not in ISLANDS:
            queue.append((i,k))
        while queue:
            i,k = queue.pop()
            visited.add((i,k))
            if (i,k) in ISLANDS or grid[i][k] == '0':
                continue
            ISLANDS.add((i,k))
            # check up
            if i - 1 < 0:
                pass
            elif (i-1,k) not in visited:
                queue.append((i-1,k))
            # check down
            if i + 1 >= len(grid):
                pass
            elif (i+1,k) not in visited:
                queue.append((i+1,k))
            # check left
            if k -1 < 0:
                pass
            elif (i,k-1) not in visited:
                queue.append((i,k-1))
            # check right
            if k + 1 >= len(grid[0]):
                pass
            elif (i,k + 1) not in visited:
                queue.append((i,k + 1))
        return ISLANDS


    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        ISLANDS = set()
        if not grid:
            return 0
        for i_idx, i in enumerate(grid):
            for k_idx, k in enumerate(i):
                if k == '1' and not self.island_exists(i_idx, k_idx, ISLANDS):
                    result += 1
                    ISLANDS = self.explore_island(i_idx, k_idx, grid, ISLANDS)
        return result
s = Solution()
r_1 = s.numIslands(grid_1)
assert r_1 == 1
r_3 = s.numIslands(grid_3)
assert r_3 == 3
