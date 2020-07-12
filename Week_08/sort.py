import pdb
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
so=Solution()
a=[5,4,6,3,7,2,8,1,9,5,4,10]
#so.mergesort(a,0,len(a)-1)
so.heepsort(a)
print(a)