#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) :
        ans=[]
        window,tar={},{}
        for char in p: tar[char]=tar.get(char,0)+1
        lens,lenp=len(s),len(p)
        right=left=0
        while right<lens:
            if s[right] not in tar:
                right=left=right+1
                window.clear()
            else:
                window[s[right]]=window.get(s[right],0)+1
                right=right+1
                if right-left==lenp:
                    if window==tar: ans.append(left)
                    window[s[left]]-=1
                    left+=1
        return ans
# @lc code=end

