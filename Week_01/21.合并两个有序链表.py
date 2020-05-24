#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 and l2 and l1.val<=l2.val:
            rst,idx_A,idx_B=l1,l1,l2
        elif l2==None:
            return l1
        else:
            rst,idx_A,idx_B=l2,l2,l1
        while(True):
            if idx_B==None:
                return rst
            elif idx_A.next and idx_A.next.val<=idx_B.val:
                idx_A=idx_A.next
            else:
                idx_tmp=idx_B.next
                idx_B.next=idx_A.next
                idx_A.next=idx_B
                idx_B=idx_tmp
                
# @lc code=end

