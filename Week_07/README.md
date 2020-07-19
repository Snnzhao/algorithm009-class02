学习笔记
	字典树和并查集
	高级搜索
		典型应用是用于统计和排序大量的字符串，所以经常被搜索引擎
		系统用于文本词频统计
		优点：最大限度地减少无谓的字符串比较，查询效率比哈希表高
		基本性质：
			1.节点本身不存完整单词；
			2.从根节点到某一结点，路径上经过的字符链接起来，为该结点
			对应的字符串；
			3.每个节点的所有子结点路径代表的字符都不相同
		核心思想：
			1.Trie树的核心思想是空间换时间
			2.利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。
		Trie 模板：
	class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root={}
        self.endword='#'


    def insert(self, word: str) :
        """
        Inserts a word into the trie.
        """
        node=self.root
        for char in word:
            node=node.setdefault(char,{})
        node[self.endword]=self.endword


    def search(self, word: str) :
        """
        Returns if the word is in the trie.
        """
        node=self.root
        for char in word:
            if char not in node:
                return False
            node=node[char]
        return self.endword in node


    def startsWith(self, prefix: str) :
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node=self.root
        for char in prefix:
            if char not in node:
                return False
            node=node[char]
        return True
		
	并查集
	Disjoint set
		解决组团和配对问题
		基本操作：makeset(x) unionSet(x,y) find(x)
	
	初级搜索：
		1.朴素搜索
		2.优化方式：不重复、剪枝 
		   搜索方向：
			深度优先搜索、广度优先搜索
			
			双向搜索、启发式搜索
			
		DFS 代码模板
			递归写法
			
			visited=set()
			
			def dfs(node, visited):
				if node in visited:
					return
				visited.add(node)
				for next_node in node.children():
					if next_node not in visited:
						dfs(next_node,visited)
						
				
				
			非递归模板：
				def DFS(self,tree):
					if tree.root is None:
						return []
					visited,stak=[],[tree.root]
					
					while stack:
						node=stack.pop()
						visited.add(node)
						process(node)
						nodes=generate_related_nodes(node)
						stack.push(nodes)
						
	剪枝
	回溯
	
	双向BFS
	模板:
				visited=set()
			
				def doubleBFS(self,graph, start, end):
					front,end={start},{end}
					while queue:
						next_front=set()
						for node in front:
							visited.add(node)
							process(node)
							nodes=generate_related_nodes(node)
							next_front.add(nodes)
						front=next_front
						if len(front)>len(back):
							front,back=back,front
							
	启发式搜索
	
	A*代码模板
	
					def AstarSearch(graph,start,end):
						pq=collections.priority_queue()
						pq.append([start])
						visited.add(start)
						
						while pq:
							node=pq.pop()
							visited.add(node)
							process(node)
							nodes-generate_related_nodes(node)
							unvisited=[node for node in nodes if node not in visites]
							pq.push(unvisited)
							
	
	高技术、AVL、红黑树
	AVL
		1.平衡二叉树
		2.每个结点存 balance_factor={-1,-0,1}
		3.四种旋转操作
		
		不足：结点需要存储额外信息，且调整次数频繁
		
	红黑树
		近似平衡二叉树，能确保任何一个结点的左右子树高度差小于两倍
					
		