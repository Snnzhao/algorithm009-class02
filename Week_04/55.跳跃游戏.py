#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) :

        #solution 1 (exceed the time)
        # isTrue=[False]*len(nums)
        # isTrue[0]=True
        # for i in range(len(nums)-1):
        #     if isTrue[i]==True:
        #         if i+nums[i]>=len(nums)-1:
        #             return True
        #         for j in range(i,i+nums[i]+1):
        #             isTrue[j]=True
        # return isTrue[-1]

        #soluion2: mark
        # maxloc=0
        # for i in range(len(nums)):
        #     if maxloc>=i and nums[i]+i>maxloc:
        #         maxloc=nums[i]+i
        # return maxloc>=len(nums)-1

        #Solution3 greedy:
        endReachable=len(nums)-1
        for i  in range(len(nums)-1,-1,-1):
            endReachable=[endReachable,i][endReachable<=i+nums[i]]
        return endReachable==0
# @lc code=end

