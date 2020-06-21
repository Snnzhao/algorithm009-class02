#
# @lc app=leetcode.cn id=529 lang=python3
#
# [529] 扫雷游戏
#

# @lc code=start
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) :
        x,y=click
        cor,col=len(board),len(board[0])
        def update(x,y):
            #terminator
            if x>cor-1 or x<0 or y>col-1 or y<0 or board[x][y]!='E':
                return
            #processor
            bumnum=0
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if 0<=i<cor and 0<=j<col:
                        bumnum=bumnum+(board[i][j]=='M')
            if bumnum==0:
                board[x][y]='B'
                #drill down
                update(x-1,y)
                update(x+1,y)
                update(x,y-1)
                update(x,y+1)
                update(x+1,y+1)
                update(x-1,y-1)
                update(x+1,y-1)
                update(x-1,y+1)
            else:
                board[x][y]=str(bumnum)
            #reverse

        if board[x][y]=='M':
            board[x][y]='X'
            return board
        else:
            update(x,y)
            return board
# @lc code=end

