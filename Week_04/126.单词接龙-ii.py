#
# @lc app=leetcode.cn id=126 lang=python3
#
# [126] 单词接龙 II
#

# @lc code=start
from collections import defaultdict,deque
from typing import List
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) :
        #solution 2: 广度优先+回溯
        word_set=set(wordList)

        #处理特殊情况
        res=[]
        if endWord not in word_set:
            return res

        #广度优先遍历获取后继节点列表
        sucessor=defaultdict(set)
        find=self._bfs(beginWord,endWord,word_set,sucessor)
        if not find:    #没有发现目标
            return res
        #回溯获取路径
        path=[beginWord]
        self._dfs(beginWord,endWord,sucessor,path,res)
        return res 

    def _bfs(self,beginWord,endWord,word_set,sucessor):
        L=len(beginWord)
        word_dic=defaultdict(set)
        self._wrddic(word_set,word_dic,L)
        #存放不能作为后继的节点（和传统意义的已访问节点意义不同）
        visited=set()
        nxtvisited=set() #当前层已经作为后继节点（在同一层可重复作为后继）
        node_son=set()
        queue=deque()
        queue.append(beginWord)
        visited.add(beginWord)
        find=False
        while queue:
            level_num=len(queue) #当前层的节点个数

            for i in range(level_num):
                node=queue.popleft()
                #生成子节点并将其送进队列
                self._findson(node,word_dic,node_son,visited)
                if endWord in node_son:
                    find=True
                for son in node_son:
                    queue.append(son)
                    sucessor[node].add(son)
                    nxtvisited.add(son)
                node_son.clear()
            visited|=nxtvisited
            nxtvisited.clear()
        return find               

    def _dfs(self,beginWord,endWord,sucessor,path,res):
        #terminator
        if beginWord==endWord:
            res.append(path.copy())
            return
        if beginWord not in sucessor:
            return
        #processor
        #drill down
        for nxtword in sucessor[beginWord]:
            path.append(nxtword)
            self._dfs(nxtword,endWord,sucessor,path,res)
            #reverse
            path.pop()
        return                                                                                                                                                                                                                                            

    def _wrddic(self,word_set,word_dic,word_len):
        for word in word_set:
            for i in range(word_len):
                word_tmp=word[:i]+'*'+word[i+1:]
                word_dic[word_tmp].add(word)
        return
    def _findson(self,node,word_dic,node_son,visited):
        L=len(node)
        for i in range(L):
            word_tmp=node[:i]+'*'+node[i+1:]
            for word in word_dic[word_tmp]:
                if word not in visited:
                    node_son.add(word)
        return
# @lc code=end

