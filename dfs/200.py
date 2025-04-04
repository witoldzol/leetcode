from typing import List
from collections import deque

grid_3 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
class Solution:
    def explore(self, coords:tuple[int,int], islands: set[tuple[int,int]], grid: list[list[str]]) -> set[tuple[int,int]]:
        visited = set()
        q = deque()
        q.append(coords)
        while q:
            i, k = q.popleft()
            visited.add((i,k))
            if grid[i][k] == '0' or (i,k) in islands:
                continue
            islands.add((i,k))
            # explore UP i
            ii = i - 1
            if ii < 0 or (ii, k) in visited or grid[ii][k] == '0':
                pass
            else:
                q.append((ii,k))
            # explore DOWN i
            ii = i + 1
            if ii >= len(grid) or (ii, k) in visited or grid[ii][k] == '0':
                pass
            else:
                q.append((ii,k))
            # explore LEFT k
            kk = k - 1
            if kk < 0 or (i, kk) in visited or grid[i][kk] == '0':
                pass
            else:
                q.append((i,kk))
            # explore RIGHT k
            kk = k + 1
            if kk >= len(grid[0]) or (i, kk) in visited or grid[i][kk] == '0':
                pass
            else:
                q.append((i,kk))
        return islands


    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ISLANDS: set[tuple[int,int]] = set()
        num_of_islands: int = 0
        for i, _ in enumerate(grid):
            for k, val in enumerate(grid[i]):
                if val == '1' and  (i,k) not in ISLANDS:
                    ISLANDS = self.explore((i, k), ISLANDS, grid)
                    num_of_islands += 1
        return num_of_islands



assert 3 == Solution().numIslands(grid_3)
