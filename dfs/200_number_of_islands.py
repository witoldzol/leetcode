grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


s = Solution()
r = s.numIslands(grid)

assert r == 1
