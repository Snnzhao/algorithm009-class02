学习笔记
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
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  
	  