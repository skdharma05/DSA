def search_element_rotated_sorted_array(nums,k):
    n = len(nums)
    low = 0
    high =n-1

    while low<= high:
        mid = (low+high)//2
        if nums[mid] == k:
            return mid
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
    return -1

def main():
    nums =[7,8,9,1,2,3,4,5,6]
    target = 1
    result = search_element_rotated_sorted_array(nums,target)
    print(result)

main()