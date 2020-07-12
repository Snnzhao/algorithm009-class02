#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
from typing import List
class Solution:
    def reversePairs(self, nums: List[int]):
        length=len(nums)
        cnt=self.mergesort(nums,0,length-1)
        return cnt
    def mergesort(self,nums,strt,end):
        if strt>=end:
            return 0
        mid=(strt+end)>>1
        cnt=self.mergesort(nums,strt,mid)+self.mergesort(nums,mid+1,end)
        i=strt
        for id2 in range(mid+1,end+1):
            while i<=mid and nums[i]<=nums[id2]*2:i+=1
            cnt+=mid-i+1
        self.merge(nums,strt,end,mid)
        return cnt
    def merge(self,nums,strt,end,mid):
        arry=[]
        id,id1=0,strt
        for id2 in range(mid+1,end+1):
            while id1<=mid and nums[id1]<=nums[id2]:
                arry.append(nums[id1])
                id1+=1
            arry.append(nums[id2])
        nums[strt:end+1]=arry+nums[id1:mid+1]
        return 
# @lc code=end