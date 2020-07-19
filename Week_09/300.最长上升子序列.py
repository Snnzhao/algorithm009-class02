#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) :
        #solution 1: DP
        #dp: 以nums[i]结尾的字符串中最长升序字串长度
        # if not nums:
        #     return 0
        # length=len(nums)
        # dp=[1]*length
        # for i in range(length):
        #     for j in range(i):
        #         if nums[i]>nums[j]:
        #             dp[i]=max(dp[j]+1,dp[i])
        # return max(dp)

        #solution 2:
        #贪婪算法+二分查找
        #d: 长度为i的升序字串中最小结尾数字
        d=[]
        length=0
        for num in nums:
            if not d or num>d[-1]:
                d.append(num)
                length=length+1
            else:
                left,right=0,length-1
                loc=right
                while(left<=right):
                    mid=(left+right)//2
                    if d[mid]<num:
                        left=mid+1
                    else:
                        loc=mid
                        right=mid-1
                d[loc]=num
        return length

        
# @lc code=end

