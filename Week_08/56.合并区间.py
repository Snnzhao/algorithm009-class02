#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) :
        intervals.sort(key=lambda x: x[0])
        merged=[]
        for inter in intervals:
            if not merged or inter[0]>merged[-1][1]:
                merged.append(inter)
            else:
                merged[-1][1]=max(inter[1],merged[-1][1])
        return merged
# @lc code=end

