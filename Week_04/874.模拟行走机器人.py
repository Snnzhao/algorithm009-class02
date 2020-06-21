#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) :
        dx,dy,x,y,dis=0,1,0,0,0
        obs_dict=set(map(tuple,obstacles))
        for cmmd in commands:
            if cmmd==-2:
                dx,dy=-dy,dx
            elif cmmd==-1:
                dx,dy=dy,-dx
            else:

                for stp in range(cmmd):
                    if (x+dx,y+dy) not in obs_dict:
                        x,y=x+dx,y+dy
                        dis=x*x+y*y if x*x+y*y>dis else dis
                    else:
                        break
        return dis

# @lc code=end

