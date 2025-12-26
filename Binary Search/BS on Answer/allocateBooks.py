class AllocateBooks:
    def _isPossible(self,arr,pages,m):
        std =1
        pages_std =0
        for page in arr:
            if pages_std + page <= pages:
                pages_std+=page
            else:
                std +=1
                pages_std = page
        return std

    def brute(self,arr,m):
        if m>len(arr):
            return -1
        
        low = max(arr)
        high = sum(arr)

        for pages in range(low,high+1):
            if self._isPossible(arr,pages,m) == m:
                return pages
        return low
    
    def Optimal(self,arr,m):
        if m>len(arr):
            return -1
        
        low = max(arr)
        high = sum(arr)
        ans = -1

        while low<=high:
            mid = (low + high)//2
            if self._isPossible(arr,mid,m) == m:
                ans =  mid
                high = mid -1
            else:
                low = mid +1
        return ans
    
arr=[10, 20, 30, 40]
m=2
allocateBooks = AllocateBooks()
print(allocateBooks.brute(arr=arr,m = m))
print(allocateBooks.Optimal(arr=arr,m = m))


"""
# LeetCode = Q 410

class Solution(object):
    def splitArray(self, nums, k):
        if k>len(nums):
            return -1

        def _isPossible(limit):
            sunarray =1
            current_sum =0

            for num in nums:
                if current_sum + num<=limit:
                    current_sum+=num
                else:
                    sunarray +=1
                    current_sum = num
            return sunarray

        low = max(nums)
        high = sum(nums)
        ans =-1

        while low<= high:
            mid = (low + high)//2
            if _isPossible(mid)<=k:
                ans = mid
                high = mid - 1
            else :
                low = mid + 1
            
        return ans

"""