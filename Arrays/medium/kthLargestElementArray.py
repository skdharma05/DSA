import heapq
class KthLargestElementArray:
    def better(self,nums,k):
        heap =[]
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap)>k:
                heapq.heappop(heap)
        return heap[0]
    
num = [3,2,1,5,6,4]
k = 2
kthLargestElementArray = KthLargestElementArray()
print(kthLargestElementArray.better(num,k))
