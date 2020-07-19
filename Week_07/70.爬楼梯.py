#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int):
#  solution 1 :recursion    exceed time
        # if n==2:
        #     return 2
        # elif n==1:
        #     return 1
        # else:
        #     return self.climbStairs(n-2)+self.climbStairs(n-1)

        if n<3: return n
        else:
            f_1,f_2,f_3=1,2,3
            for i in range(3,n+1):
                f_3=f_1+f_2
                f_1=f_2
                f_2=f_3
            return f_3
# @lc code=end

