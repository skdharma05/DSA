def brute_single_element_sorted_array(nums):
    
    n = len(nums)
    if n ==1:
        return nums[0]
    
    for i in range (n):
        if i ==0: # First element
            if nums[i] != nums[i+1]:
                return nums[i]
        elif i == n-1: # Last element
            if nums[i] != nums[i-1]:
                return nums[i]
        else: # Middle elements
            if nums[i] != nums[i+1] and nums[i]!= nums[i-1]:
                return nums[i]

def Optimal_single_element_sorted_array(nums):
    n= len(nums)
    if n == 1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n-1]!= nums[n-2]:
        return nums[n-1]
    low = 1
    high = n-2
    while low<=high:
        mid = (low+high)//2
        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        if (mid % 2 == 1 and nums[mid] == nums[mid-1] ) or (mid %2 ==0 and nums[mid]==nums[mid+1]) :
            low = mid +1
        else:
            high = mid -1

def main():
    nums = [1,1,2,3,3]
    result = Optimal_single_element_sorted_array(nums)
    print(result)
main()