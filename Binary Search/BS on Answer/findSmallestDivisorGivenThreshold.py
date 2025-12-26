import math 
class SmallestDivisor:
    def brute(self,nums,threshold):
        n = len(nums)
        for d in range(1,max(nums)+1):
            sumi =0
            for num in nums:
                sumi+=(num + d -1)//d
            if sumi<=threshold:
                return d
        return -1
    def optimal(self,nums,threshold):
        low = 1
        high = max(nums)
        ans = -1
        while low<=high:
            mid = (low+high)//2
            sumi =0
            for num in nums:
                sumi = sumi+(num+mid-1)//mid 
            if sumi<=threshold:
                ans = mid
                high = mid -1
            else:
                low = mid +1
        return ans

nums = [1,2,5,9]
threshold = 6
smallestDivisor = SmallestDivisor()

print(smallestDivisor.brute(nums , threshold))
print(smallestDivisor.optimal(nums,threshold))



