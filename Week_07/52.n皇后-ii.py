#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N皇后 II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) :
        return self.dfs(n,0,0,0,0)
    def dfs(self,n,row,que,pie,na):
        if row==n:
            return 1
        cnt=0
        for s in range(n):
            po=1<<s
            if not (po&que or po&pie or po&na):
                cnt+=self.dfs(n,row+1,que|po,(pie|po)>>1,(na|po)<<1)
        return cnt
        
# @lc code=end

