#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mdval=[]
        lgth=len(nums)
        k=k%lgth
        for i in range(lgth-k,lgth):
            mdval.append(nums[i])
        for i in range(lgth-1,k-1,-1):
            nums[i]=nums[i-k]
        for i in range(k):
            nums[i]=mdval[i]
        # @lc code=end

