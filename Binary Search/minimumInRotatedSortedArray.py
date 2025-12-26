def min_value_in_rotared_sorted_array(nums):
    n= len(nums)
    low = 0
    high = n-1
    ans = float('inf')
    while low<=high:
        if nums[low]<=nums[high]:
            ans = min(ans,nums[low])
            break
        mid = (low+high)//2

        if nums[low]<=nums[mid]:
            ans = min(ans,nums[low])
            low = mid +1
        else:
            ans = min(ans,nums[mid])
            high = mid-1
    return ans

def main():
    nums = [4,5,6,7,1,2]
    result = min_value_in_rotared_sorted_array(nums)
    print(result)
main()