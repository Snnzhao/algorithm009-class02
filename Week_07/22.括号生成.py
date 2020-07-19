#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    rst=[]
    def generateParenthesis(self, n: int):
    # solution 1:递归+减枝
    #     self.rst=[]
    #     self._generate(0,0,n,'')
    #     return self.rst

    # def _generate(self, left: int, right: int, max: int, strng: str):
    #     #terminal
    #     if left==right and left==max:
    #         self.rst.append(strng)
    #         return
    #     #process
    #     #drill down
    #     if left<max:
    #         self._generate(left+1,right,max,strng+'(')
    #     if right<left:
    #         self._generate(left,right+1,max,strng+')')
        
    #     #reverse
    #     return

    #solution 2: DP
    
# @lc code=end

