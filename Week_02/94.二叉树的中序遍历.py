#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) : 
        
        #Solution1:递归
        # res=[]

        # def helper(root):
        #     if root:
        #         helper(root.left)
        #         res.append(root.val)
        #         helper(root.right)
        # helper(root)
        # return res
        
        #Solution2 :颜色标记法
        # WHITE,GRAY=0,1
        # res=[]
        # stack=[(WHITE,root)]
        # while stack:
        #     color,node=stack.pop()
        #     if node==None:
        #         continue
        #     if color==WHITE:
        #         stack.append((WHITE,node.right))
        #         stack.append((GRAY,node))
        #         stack.append((WHITE,node.left))
        #     else:
        #         res.append(node.val)
        # return reser

        #solution3： 维护栈
        res,stack=[],[]
        cur=root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            res.append(cur.val)
            cur=cur.right
        return res            


# @lc code=end

