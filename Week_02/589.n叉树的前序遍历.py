#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        #solution1 递归
        # res=[]
        # def helper(root):
        #     if root:
        #         res.append(root.val)
        #         for child in root.children:
        #             helper(child)
        # helper(root)

        #solution 2 维护栈
        if root==None:
            return []
        res,stack=[],[root]
        while stack:
            cur=stack.pop()
            res.append(cur.val)
            for child in cur.children[::-1]:
                stack.append(child)
        return res
# @lc code=end

