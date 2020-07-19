#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
import collections
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]):
        if end not in bank:
            return -1
        length=len(start)
        genemap=collections.defaultdict(set)
        for gene in bank:
            for i in range(length):
                genetmp=gene[:i]+'*'+gene[i+1:]
                genemap[genetmp].add(gene)
        
        front,back={start},{end}
        visited=set()
        level=0
        while front:
            level+=1
            next_front=set()
            for node in front:
                for i in range(length):
                    genetmp=node[:i]+'*'+node[i+1:]
                    for gene in genemap[genetmp]:
                        if gene in back:
                            return level
                        if gene not in visited:
                            visited.add(gene)
                            next_front.add(gene)
            front=next_front
            if len(front)>len(back):
                front,back=back,front
        return -1
# @lc code=end

