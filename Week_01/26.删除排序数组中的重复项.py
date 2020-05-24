#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx_fwd,idx_bkd=0,0
        for idx_fwd in range(1,len(nums)):
            if (nums[idx_bkd]!=nums[idx_fwd]):
                idx_bkd+=1
                nums[idx_bkd]=nums[idx_fwd]
        return idx_bkd+1
# @lc code=end

