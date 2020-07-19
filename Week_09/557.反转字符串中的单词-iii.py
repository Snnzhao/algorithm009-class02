#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) :
        strl=s.split()
        return " ".join([char[::-1] for char in strl])
# @lc code=end

