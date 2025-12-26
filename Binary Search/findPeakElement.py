class Peak:
    def brute_find_peak_element(self,nums):
        n = len(nums)
        for i in range(n):
            left = (i == 0 or nums[i]>nums[i-1])
            right = (i==n-1 or nums[i]>nums[i+1])
            if left and right:
                return i
    
    def optimal_find_peak_element(self,nums):
        n= len(nums) 

        if n==1:
            return 0
        if nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        
        low = 1
        high = n-2
        while low<=high:
            mid = (low+high)//2
            if nums[mid-1]<nums[mid]and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]<nums[mid+1]:
                low = mid +1
            else:
                high = mid -1
        return None
            
            
nums = [1, 3, 4, 5, 6]
peak_finder= Peak()
peak_index = peak_finder.optimal_find_peak_element(nums)
print("A peak element is at index:", peak_index)
print("Peak element value:", nums[peak_index])
