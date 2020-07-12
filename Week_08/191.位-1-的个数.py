#
# @lc app=leetcode.cn id=191 lang=python3
#
# [191] 位1的个数
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) :
        n=bin(n)
        count=0
        while(n):
            n=n&(n-1)
            count=count+1
        return count
        
# @lc code=end

