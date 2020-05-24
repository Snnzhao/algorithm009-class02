#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        left,right,hgt=0,len(height)-1,1
        Sum,tmp=0,0
        while(left<=right):
            while(left<=right and height[left]<hgt):
                Sum+=height[left]
                left+=1
            while(left<=right and height[right]<hgt):
                Sum+=height[right]
                right-=1
            tmp+=right-left+1
            hgt+=1
        return tmp-Sum
# @lc code=end

