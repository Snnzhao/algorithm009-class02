学习笔记
	深度优先搜索和广度优先搜索
	
	深度优先遍历
		DFS代码模板：
		递归写法：
			visited=set()
			
			def dfs(node, visited):
				if node in visited: #terminator
					return
					
				visited.add(node)
				
				dfs(node.left)
				dfs(node.right)
				
		非递归写法：
			def DFS(self, tree):
				if tree.root is None:
					return []
				
				visited,stack=[],[tree.root]
				
				while stack:
					node=stack.pop()
					visited.add(node)
					process(node)
					nodes=generate_related_nodes(node)
					stack.push(nodes)
					
		广度优先遍历
			visited=set()
			
				def BFS(self,graph, start, end):
					queue=[]
					queue=queue+[start]
					while queue:
						node=queue.pop()
						visited.add(node)
						process(node)
						nodes=generate_related_nodes(node)
						stack.push(nodes)
	

	贪心算法：
		每步当下情况走最优以求全局最优
		贪心算法和动态规划的区别：
			贪心算法每一步都做出决策而动态会保存当前结果并根据之前的结果对当下做出选择
			有回退功能
			
			贪心：当下局部最优判断
			回溯：能够回退
			动态规划：最有判断+回退
		贪心算法在实际应用中往往无法达到最优，但因为其高效和接近最优，往往用来作辅助判断
		
		适用于贪心算法的情况：
		  问题可以分成子问题来解决，子问题的最优解能递推到最终问题的最优解。（称为最优子结构）
		  
	二分查找：
		前提条件：
			目标单调性、存在上下界、能通过索引访问
			
		模板：
			left,right=0,len(array)-1
			while left<=right:
				mid=(left+right)/2
				if array[mid]==target:
					break or return result
					
				elif array[mid]<target:
					left=mid+1
				else:
					right=mid-1
		