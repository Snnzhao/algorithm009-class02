#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
import collections
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) :
        worddict=collections.defaultdict(list)
        L=len(beginWord)
        for word in wordList:
            for i in range(L):
                wordtmp=word[:i]+'*'+word[i+1:]
                worddict[wordtmp].append(word)
        visited=[beginWord]
        level=1
        queue=collections.deque()
        queue.append((level,beginWord))

        while queue:
            level,word=queue.popleft()
            if word==endWord:
                return level
            for i in range(L):
                wordtmp=word[:i]+'*'+word[i+1:]
                for newword in worddict[wordtmp]:
                    if newword not in visited:
                        visited.append(newword)
                        queue.append((level+1,newword))
        return 0
# @lc code=end

