#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) :
        rt=""
        for i in range(0,len(s),k*2):
            rt+=s[i:i+k][::-1]+s[i+k:i+2*k]
        return rt
        
# @lc code=end

