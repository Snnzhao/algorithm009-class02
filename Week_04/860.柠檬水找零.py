#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) :
        cllctn={5:0,10:0,20:0}

        def change(bill):
            if bill==5:
                cllctn[bill]=cllctn[bill]+1
                return  True
            else:
                rst=bill-5
                if cllctn[10]>=rst//10:
                    cllctn[10],rst=cllctn[10]-rst//10,rst%10
                if cllctn[5]>=rst//5:
                    cllctn[5],rst=cllctn[5]-rst//5,rst%5
                if rst==0:
                    cllctn[bill]=cllctn[bill]+1
                    return True
                else:
                    return False

        for i in range(len(bills)):
            if not change(bills[i]):
                return False
        return True
# @lc code=end

