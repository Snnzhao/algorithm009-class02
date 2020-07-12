#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) :
        bucket=[0]*1001
        for num in arr1:
            bucket[num]+=1
        id=0
        for num2 in arr2:
            while bucket[num2]>0:
                arr1[id]=num2
                bucket[num2]-=1
                id+=1
        for num1 in range(1001):
            while bucket[num1]>0:
                arr1[id]=num1
                bucket[num1]-=1
                id+=1
        return arr1
# @lc code=end

