#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode):
        #solution 1: 递归
        # res=[]
        # def helper(root):
        #     if root:
        #         res.append(root.val)
        #         helper(root.left)
        #         helper(root.right)
        # helper(root)
        # return res

        #solution2 :维护栈
        res,stack=[],[]
        cur=root
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            cur=cur.right
        return res
# @lc code=end

