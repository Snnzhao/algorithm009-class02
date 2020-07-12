#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) :
        length=len(s)
        nums=[1]*length
        if len(nums)==0:
            return 0
        for i in range(length-1):
            if int(s[i:i+2])<=26:
                nums[i]=2
        for i in range(length-1):
            if int(s[i])==0:
                nums[i]=0
        nums.append(1)
        for i in range(length-1,-1,-1):
            if int(s[i])==0:
                nums[i]=0
            elif nums[i]==1:
                nums[i]=nums[i+1]
            else:
                nums[i]=sum(nums[i+1:i+3])
        return nums[0]
# @lc code=end

