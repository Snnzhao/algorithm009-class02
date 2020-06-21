#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        cor,col=len(matrix), len(matrix[0])
        def DtoDD(idx):
            return (idx//col,(idx+1)%col-1)
        left,right=0,cor*col-1
        while left<=right:
            mid=(left+right)//2
            cor_mid,col_mid=DtoDD(mid)
            if matrix[cor_mid][col_mid]==target:
                return True
            elif matrix[cor_mid][col_mid]<target:
                left=mid+1
            else:
                right=mid-1
        return False
# @lc code=end

