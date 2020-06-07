#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        
        left_res = self.lowestCommonAncestor(root.left, p, q)
        right_res = self.lowestCommonAncestor(root.right, p, q)
        
        if (left_res and right_res) or (root in [p, q]):
            return root
        else:
            return left_res or right_res
# @lc code=end

