#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) :
        return sum(a-b for  a,b in zip(prices[1:],prices[0:-1]) if a>b)
# @lc code=end

