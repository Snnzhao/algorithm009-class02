#
# @lc app=leetcode.cn id=641 lang=python3
#
# [641] 设计循环双端队列
#

# @lc code=start
import collections
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.dq=collections.deque(maxlen=k)

    def insertFront(self, value: int):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.dq)<self.dq.maxlen:
            self.dq.appendleft(value)
            return True
        else:
            return False

    def insertLast(self, value: int):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.dq)<self.dq.maxlen:
            self.dq.append(value)
            return True
        else:
            return False
        

    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.dq)==0:
            return False
        else:
            self.dq.popleft()
            return True
        

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.dq)==0:
            return False
        else:
            self.dq.pop()
            return True
        

    def getFront(self):
        """
        Get the front item from the deque.
        """
        return self.dq[0] if len(self.dq)!=0 else -1
        

    def getRear(self):
        """
        Get the last item from the deque.
        """
        return self.dq[-1] if len(self.dq)!=0 else -1

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        """
        return len(self.dq)==0

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        """
        return len(self.dq)==self.dq.maxlen


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
# @lc code=end

