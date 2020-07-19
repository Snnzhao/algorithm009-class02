#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) :
        stl=list(str.strip())
        if not stl:
            return 0
        sign=-1 if stl[0]=='-' else 1
        if stl[0] in ('-','+'): del stl[0]
        rtn=0
        for char in stl:
            if char.isdigit():
                rtn=rtn*10+ord(char)-ord('0')
            else:
                break
        return max(min(sign*rtn,2**31-1),-2**31)
# @lc code=end

