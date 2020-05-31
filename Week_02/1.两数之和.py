#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):

        #solution 3
        obsrve={}
        for t in range(len(nums)):
            if nums[t] not in obsrve:
                obsrve[target-nums[t]]=t
            else:
                return [t, obsrve[nums[t]]]
# @lc code=end

