#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        idx=1
        for idx in range(1,len(digits)+1):
            if carry==0:
                return digits
            carry,digits[-idx]=(digits[-idx]+carry)//10,(digits[-idx]+carry)%10
        if carry==1:
            digits.insert(0,1)
        return digits
# @lc code=end

