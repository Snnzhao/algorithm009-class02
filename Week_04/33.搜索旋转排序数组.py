#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) :
        if len(nums)<=0:
            return -1
        lo,hi=0,len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]==target:
                return mid
            elif (nums[mid]>=nums[0] and (target<nums[0] or target >nums[mid])) \
            or (nums[mid]<nums[0] and(target<nums[0] and target>nums[mid])):
                lo=mid+1
            else:
                hi=mid-1
        return -1
# @lc code=end

