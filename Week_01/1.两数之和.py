#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):

        #solution 3
        observe={}
        for i in range(len(nums)):
            if nums[i] not in observe.keys():
                observe[target-nums[i]]=i
            else:
                return [observe[nums[i]],i]
        return []
# @lc code=end

