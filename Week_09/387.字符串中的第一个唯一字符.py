#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
import collections
class Solution:
    def firstUniqChar(self, s: str) :
        hashmap={}
        for char in s:
            if char not in hashmap:
                hashmap[char]=1
            else:
                hashmap[char]+=1
        for i in range(len(s)):
            if hashmap[s[i]]==1:
                return i
        return -1
# @lc code=end

