#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) :
        g.sort()
        s.sort()
        num_s,num_g=len(s),len(g)
        id_g=0
        for id_s in range(num_s):
            if id_g==num_g:
                return num_g
            if g[id_g]<=s[id_s]:
                id_g=id_g+1

        return id_g
# @lc code=end

