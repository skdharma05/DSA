def search_element_rotated_sorted_array_dup(nums,k):
    n = len(nums)
    low = 0
    high =n-1

    while low<= high:
        mid = (low+high)//2
        if nums[mid] == k:
            return True
        if nums[low]==nums[mid] and nums[mid]==nums[high]:
            low= low+1
            high = high -1
            continue
        if nums[low]<=nums[mid]:
            if nums[low]<=k and k <=nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if nums[mid]<=k and k<=nums[high]:
                low = mid+1
            else:
                high = mid-1
    return False

def main():
    nums =[2,5,6,0,0,1,2]
    target = 9
    result = search_element_rotated_sorted_array_dup(nums,target)
    print(result)

main()