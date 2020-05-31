#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
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
    def postorder(self, root: 'Node'):
        #solution 1 递归
        # res=[]
        # def helper(root):
        #     if root:
        #         for child in root.children:
        #             helper(child)
        #         res.append(root.val)
        # helper(root)
        # return res

        #solution 2 维护栈
        if root==None:
            return []
        res,stack=[],[root]
        while stack:
            cur=stack.pop()
            res.append(cur.val)
            for child in cur.children:
                stack.append(child)
        return res[::-1]
# @lc code=end

