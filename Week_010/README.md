期末总结
1.四个一维数据结构：        数组、    链表、     栈、     队列    
			     空间复杂度 O(n)       O(n)      O(n)     O(n)
			查询时间复杂度	O(1)       O(n)      O(n)     O(n)
		插入删除空间复杂度	O(n)       O(1)      O(1)     O(1)

2.队列优化：优先队列
            插入：O(1)  取出O(logn)
3.链表的优化：跳表
		（空间换时间）查询,插入删除时间复杂度log(n)
	相比于红黑树 优点：节省内存，
						更易读，实现更简单更方便debug
						操作相对局部，在并行环境下更加适用
				 缺点：维护成本高

4.算法技巧：
       （1）双指针   移动零
	   （2）栈剥洋葱 有小括号
	   （3）递归思想 爬楼梯
	   
哈希表、映射、集合：
	Hash table
		散列函数：将关键码值映射到对应的位置。
		Hash Collisions:
			solution: 后放、拉链式
			
收集精选代码的习惯

树，二叉树，二叉搜索树
	链表的next指针编程多个就变成树了（核心思想：升维来加速）
	树和图的区别在于是否有环
	树的出发点：生活中很多问题的解决方式是树形结构的
	树的遍历：
		前序：根-左-右
		中序：左-根-右
		后序：左-右-根
	
	树的面试题解法一般都是递归，为什么？
		树本身的结构无法有效的遍历:没有后继结构或是便于循环的结构
	
	二叉搜索树：
		左子树节点值小于根节点、右子树的值大于根节点
		中序遍历：升序排列
		插入和查询操作都是log2(n)
		
		
堆和二叉堆：
	堆：可以迅速找到一堆数中最大值或者最小值的数据结构
	常见的堆有二叉堆和斐波拉契堆
	二叉堆：
		通过完全二叉树来实现
		任何节点的值>=儿子节点
		可以直接一维数组来实现
		
		结点 i左儿子2*+1 右儿子2*i+2
			父结点（i-1）/2
	
图的实现和特性：
	图的属性和分类
	
递归 Recursion
	递归结构： recursion terminator、process logical in current level
	           drill down 、revert the  current level status if needed
	递归要点：1不要人肉递归 2找最近最简单子方法 3数学归纳法思维
	
	递归模板：
	const recursion = function(level, param1, param2, ...) {
    if (level > MAX_LEVEL) {
         // process result 
         return; 
    }
    // process current logic 
    process(level, param);

  // drill down 
  recur( level: level + 1, newParam); 
  // restore current status 
  }
	爬楼梯问题：

分治、回溯的实现和特性
	分治和递归本质上都是找问题的重复性并分解问题
	
	分治代码模板：
		recursion terminator、prepare data、 conquer subproblems、 process and generate the 
		final result
		
		def divide conquer(problem, param1, param2,...)
			#recursion terminator
			if problem is None:
				print_result
				return
			#prepare data
			data=prepare_data(problem)
			subproblems=split_problem(problem, data)
			
			#conquer subproblems
			subresult1=self_divide_conquer(subproblems[0],p1,...)
			subresult2=self_divide_conquer(subproblems[1],p1,...)
			...
			
			#process and generate the final result
			result=process_result(subresult1,subresult2,...)


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
		
		
动态规划
	动态规划是一种将复杂问题简化为递归子问题的方式
	分治+最优子结构
	
	动态规划和递归和分治没有根本上的区别 （关键是看有无最优子结构）
	共性：找到重复子问题
	差异性：最优子结构、中途可以淘汰次优解
	
	实战例题
	  斐波拉契数列： 
		傻递归：指数级
	    动态规划：用数组储存中间结果    自顶向下
		直接用循环加数组  				自低向上    （动态地推DP）
	
	  路径计数
	  最长公共子序列：
		
	动态规划关键点
		最优子结构
		储存中间状态
		递推公式
		
		
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
		
   位运算
		XOR -异或
			x^0=x
			x^1s=~x
			x^(~x)=1s
			x^x=0
		常用的位运算：
			1.将x最右边的n位清零：x&(~0<<n)
			2.获取x的第n位值：（x>>n)&1
			3.获取x的第n位幂的值: x&(1<<n)
			4.仅将第n位置为1：x|(1<<n)
			5.仅将第n位置为0：x&(~(1<<n))
			6.将x最高位至第n位清零：x&((1<<n)-1)
			
		实战位运算要点：
			判断奇偶：
			（x&1)==1 奇
			（x&1)==0 偶
			
			x/2：
			x=x>>1
			
			清零最低位的1：
			x=x&(x-1)
			
			获得最低位的1：
			x&(-x)
			
	布隆过滤器（Bloom filter）：
		HashTable+拉链存储重复元素
		
		Bloom Filter vs Hash Table
			一个很长的二进制向量和一系列随机映射函数。布隆过滤器可以用
			于检索一个元素是否在一个集合中
			
			有点是空间效率和查询时间都远远超过一般的算法
			缺点是有一定的误识别率和删除困难
				不在一定是不在，在不一定是在
				
			案例：1比特币、分布式系统（Map-Reduce）--Hadoop、 search engine
			      Redis缓存、垃圾邮件评论等过滤
	  
	  
	LRU Cache:
		Cache 缓存
		
	排序算法
		
		（非线性时间）比较类&（线性时间）非比较类 
		  不可突破nlogn         可以突破nlogn
		                        只可以处理整型
								需要用特殊的内存空间
		
		nlogn的排序：堆排序、快速排序、归并排序
		
		初级排序（n^2）
			选择排序：每次找最小的值放在待排序数组的起始位置
			插入排序：从前到后逐步构建有序序列：对于未排序数据，在已排序
			序列中从后向前扫描，找到相应的位置并插入
			冒泡排序：嵌套循环，每次查看相邻元素，如果逆序，则交换
			
from queue import PriorityQueue
class Solution:
    def bubble_sort(self,nums):
        length=len(nums)
        for i in range(length-1):
            ischaos=False
            for j in range(0,length-1-i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
                    ischaos=True
            if ischaos==False:
                break
        return

    def Selec_sort(self,nums):
        length=len(nums)
        for i in range(length-1):
            min_id=i
            for j in range(i+1,length-1):
                if nums[j]<nums[min_id]:
                    min_id=j
            nums[i],nums[min_id]=nums[min_id],nums[i]
        return

    def Insert_sort(self,nums):
        length=len(nums)
        for i in range(1,length):
            cur=nums[i]
            pre=i-1
            while pre>=0 and nums[pre]>cur:
                nums[pre+1]=nums[pre]
                pre=pre-1
            nums[pre+1]=cur   
        return

    def quick_sort(self,nums,start,end):
        if start>=end:
            return
        part=self.partition(nums,start,end)
        self.quick_sort(nums,start,part-1)
        self.quick_sort(nums,part+1,end)
        return

    def mergesort(self,nums,start,end):
        if start>=end:
            return
        mid=(start+end)>>1
        self.mergesort(nums,start,mid)
        self.mergesort(nums,mid+1,end)
        self.merge(nums,start,end,mid)
        return

    def heepsort(self,nums):
        length=len(nums)
        pq=PriorityQueue()
        for num in nums:
            pq.put(num)
        for i in range(length):
            nums[i]=pq.get()
        return

    def partition(self,nums,start,end):
        count,pivot=start,end
        for i in range(start,end):
            if nums[i]<nums[pivot]:
                nums[count],nums[i]=nums[i],nums[count]
                count=count+1
        nums[count],nums[pivot]=nums[pivot],nums[count]
        return count

    def merge(self,nums,start,end,mid):
        arry=[0]*(end-start+1)
        id,id1,id2=0,start,mid+1
        while id1<=mid and id2<=end:
            if nums[id1]<=nums[id2]:
                arry[id]=nums[id1]
                id1,id=id1+1,id+1
            else:
                arry[id]=nums[id2]
                id2,id=id2+1,id+1
        while id1<=mid:
            arry[id]=nums[id1]
            id,id1=id+1,id1+1
        while id2<=end:
            arry[id]=nums[id2]
            id,id2=id+1,id2+1
        nums[start:end+1]=arry
        return
	  
	  
动态规划、状态转移方程
高级动态规划
	复杂来源：
		1.状态拥有更多维度
		2.状态方程更加复杂
		
	不同路径二:
	    状态转移方程：dp[i][j]=(dp[i-1][j]+dp[i][j-1])(1-dp[i][j])
字符串
	python、java的string是不可变的
	当对其进行编辑的时候，实际上是新生成了一个string
	
高级 字符串算法
	最长子串、子序列
	
	字符串匹配算法：
		1.暴力法
		2.Rabin-Karp算法
			子串的哈希值先比对，一样再逐个比较
		3.KMP算法
		    移动位数 = 已匹配的字符数 - 对应的部分匹配值
		4.Boyer-Moore算法：
			坏字符规则和好后缀规则