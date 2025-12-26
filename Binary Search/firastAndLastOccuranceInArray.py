def brut_first_last_position_element_sortedArray(nums,targert):
    first = -1
    last =-1

    for i in range(len(nums)):
        if nums[i]==targert:
            if first == -1:
                first = i
            last =i
    
    return [first, last]


def optimal_first_last_position_element_sortedArray(nums,target):
    n = len(nums)
    #first
    low =0
    high = n-1
    first =-1

    while low<=high:
        mid = (low+high)//2
        if nums[mid]== target:
            first = mid
            high = mid -1
        elif nums[mid]<target:
            low = mid+1
        else:
            high = mid -1

    #last
    low =0
    high =n-1
    last =-1
    while low<=high:
        mid = (low+high)//2
        if nums[mid]== target:
            last = mid
            low = mid +1
        elif nums[mid]<target:
            low = mid+1
        else:
            high = mid -1
    return [first,last]
def main():
    nums = [5,7,7,8,8,8,10]
    target = 10
    result = optimal_first_last_position_element_sortedArray(nums,target)
    print(result)
main()