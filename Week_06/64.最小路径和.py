#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) :
        if not grid or not grid[0]:
            return 0
        m,n=len(grid),len(grid[0])
        if m==0 or n==0:
            return sum([sum(grid[i]) for i in range(m)])
        for i in range(m-2,-1,-1):
            grid[i][-1]+=grid[i+1][-1]
        for j in range(n-2,-1,-1):
            grid[-1][j]+=grid[-1][j+1]
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                grid[i][j]+=min(grid[i+1][j],grid[i][j+1])
        return grid[0][0]
# @lc code=end

