#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return
        idx1,idx2,idx3=m-1,n-1,m+n-1
        while(idx2>=0 and idx3>=0):
            if idx1<0 or nums1[idx1]<=nums2[idx2]:
                nums1[idx3]=nums2[idx2]
                idx3,idx2=idx3-1,idx2-1
            else:
                nums1[idx3]=nums1[idx1]
                idx1,idx3=idx1-1,idx3-1
# @lc code=end

