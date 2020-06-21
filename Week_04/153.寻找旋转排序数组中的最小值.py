#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) :
        #solution 1: 二分+判断序列单调性
        # minum=nums[0]
        # left,right=0,len(nums)-1
        # while left<=right:
        #     mid=(left+right)//2
        #     if nums[mid]>=nums[left]:
        #         minum=minum if minum<=nums[left] else nums[left]
        #         left=mid+1
        #     else:
        #         minum=minum if minum<=nums[mid] else nums[mid]
        #         right=mid-1
        # return minum

        #solution 1: 二分+判断序列旋转点
        minum=nums[0]
        left,right=0,len(nums)-1
        if nums[left]<=nums[right]:
            return nums[left]
        while left<=right:
            mid=(left+right)//2
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            if nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid]>=nums[left]:
                left=mid+1
            else:
                right=mid-1
        return minum
# @lc code=end

