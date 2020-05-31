#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
import heapq as hq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        fre={}
        for num in nums:
            if num not in fre:
                fre[num]=1
            else:
                fre[num]+=1
        que=[]
        for num,freq in fre.items():
            hq.heappush(que,(freq,num))
            if len(que)>k:
                hq.heappop(que)
        while que:
            res.append(hq.heappop(que)[1])
        return res
# @lc code=end

