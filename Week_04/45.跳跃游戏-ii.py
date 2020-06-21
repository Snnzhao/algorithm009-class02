#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
from collections import deque
class Solution:
    def jump(self, nums: List[int]) :
        #广度优先遍历 time exceed
        # level=0
        # queue=deque()
        # queue.append((level,0))
        # end=len(nums)-1
        # visited=set()
        # while queue:
        #     level,cur=queue.popleft()
        #     if cur>=end:
        #         return level
        #     for i in range(nums[cur],0,-1):
        #         if i+cur not in visited:
        #             queue.append((level+1,i+cur))
        #             visited.add(i+cur)

        #Solution 2: greedy
        cur=0
        level=0
        end=len(nums)-1
        while cur<end:
            if nums[cur]+cur>=end:
                return level+1
            nxcur=cur+nums[cur]
            nx2cur=nxcur+nums[nxcur]
            for i in range(1,nums[cur]):
                if cur+i+nums[cur+i]>nx2cur:
                    nxcur=cur+i
                    nx2cur=nxcur+nums[nxcur]
            cur=nxcur
            level=level+1
        return level
# @lc code=end

