#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) :
        def Mrkdwn(col,vol):
            if col<0 or vol<0 or col>len(grid)-1 or vol>len(grid[0])-1or grid[col][vol]=='0':
                return
            grid[col][vol]='0'
            Mrkdwn(col-1,vol)
            Mrkdwn(col+1,vol)
            Mrkdwn(col,vol-1)
            Mrkdwn(col,vol+1)
            return
        col=len(grid)
        if col==0:
            return 0
        vol=len(grid[0])
        num=0
        for i in range(col):
            for j in range(vol):
                if grid[i][j]=='1':
                    num=num+1
                    Mrkdwn(i,j)
        return num
# @lc code=end

