from typing import List
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
ISLANDS = set()
class Solution:
    def not_in_existing_island(self, i: int, k: int) -> bool:
        return True

    def explore_island(self, i: int, k: int) -> tuple[int,int,int]:
        # bfs

    def numIslands(self, grid: List[List[str]]) -> int:
        g_len = len(grid)
        g_wid = len(grid[0])
        print(g_len)
        print(g_wid)
        for i_idx, i in enumerate(grid):
            for k_idx, k in enumerate(i):
                if k == 1 and self.not_in_existing_island(i_idx, k_idx):
                    ISLANDS.add(self.explore_island(i_idx, k_idx))
# if we walk from 0,0 ... to 0,n and look for a land
# when we find it, we dfs until we get the borders
# we save the borders in a map: set( tuples of coords )
# 
# we continue then row by row, and if we find 1, we check if it falls into existing island ) ( this can be very expensive )

s = Solution()
r = s.numIslands(grid)

assert r == 1
