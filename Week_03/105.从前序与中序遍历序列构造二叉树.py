#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def handle(self, preorder: List[int], pre_begin: int, inorder: List[int], in_begin:int, length: int, idx: Dict[int, int]) -> TreeNode:
        if length == 0:
            return None
        pvoit = idx[preorder[pre_begin]]
        l = pvoit - in_begin
        ret = TreeNode(preorder[pre_begin])
        ret.left = self.handle(preorder, pre_begin + 1, inorder, in_begin, l, idx)
        ret.right = self.handle(preorder, pre_begin + l + 1, inorder, in_begin + l + 1, length - l - 1, idx)

        return ret

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        idx = dict()
        for i in range(len(inorder)):
            idx[inorder[i]] = i

        return self.handle(preorder, 0, inorder, 0, len(inorder), idx)

# @lc code=end

