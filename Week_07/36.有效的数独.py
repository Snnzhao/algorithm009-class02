#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) :
        for i in range(9):
            nums1,nums2,nums3=[],[],[]
            for j in range(9):
                if board[i][j]!=".":
                    if board[i][j] not in nums1:
                        nums1.append(board[i][j])
                    else:
                        return False
                if board[j][i]!=".":
                    if board[j][i] not in nums2:
                        nums2.append(board[j][i])
                    else:
                        return False
                if board[3*(i//3)+j//3][3*(i%3)+(j%3)]!=".":
                    if board[3*(i//3)+j//3][3*(i%3)+(j%3)] not in nums3:
                        nums3.append(board[3*(i//3)+j//3][3*(i%3)+(j%3)])
                    else:
                        return False
        return True
        
# @lc code=end

