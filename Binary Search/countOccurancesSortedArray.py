def count_occurrences_in_sorted_array(arr,target):
    n = len(arr)
    low = 0
    high = n-1
    first = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==target:
            first = mid
            high = mid -1
        elif arr[mid]<target:
            low = mid+1
        else:
            high = mid-1
    
    if first == -1:
        return -1
    
    low = 0
    high = n-1
    last = -1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]==target:
            last = mid
            low = mid +1
        elif arr[mid]<target:
            low = mid+1
        else:
            high = mid-1
    
    return last-first+1

def main():
    nums = [5,7,7,8,8,8,10]
    target = 8
    result = count_occurrences_in_sorted_array(nums,target)
    print(f'The {target} occurrences in {result} times in a array')
main()