#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) :
        if (not matrix) or (not matrix[0]):
            return 0
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                matrix[i][j]=int(matrix[i][j])
        for ma in matrix:
            ma.append(0)
        matrix.append([0]*(n+1))
        mlen=0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                matrix[i][j]=matrix[i][j]*(min(matrix[i+1][j],matrix[i+1][j+1],matrix[i][j+1])+1)
                mlen=max(mlen,matrix[i][j])
        return mlen*mlen
# @lc code=end

