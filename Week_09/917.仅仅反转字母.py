#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, S: str) :
        if not S:
            return ""
        ans=[]
        j=len(S)-1
        for i, x in enumerate(S):
            if x.isalpha():
                while not S[j].isalpha():
                    j=j-1
                ans.append(S[j])
                j=j-1
            else:
                ans.append(x)
        return ''.join(ans)
        
# @lc code=end

