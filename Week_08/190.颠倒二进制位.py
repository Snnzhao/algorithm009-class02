#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] 颠倒二进制位
#

# @lc code=start
class Solution:
    def reverseBits(self, n: int) :
        #solution 1
        #return int('0b'+('0'*32+bin(n)[2:])[-32:][::-1],base=2)

        #solution 2
        res=0
        for i in range(32):
            res|=(n&1)<<(31-i)
            n=n>>1
        return res
# @lc code=end

