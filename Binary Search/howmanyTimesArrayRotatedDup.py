def how_many_times_array_rotared_with_duplicates(nums):
    n= len(nums)
    low = 0
    high = n-1
    ans = float('inf')
    index =-1
    while low<=high:

        if nums[low]<=nums[high]:
              if nums[low]<ans:
                ans = nums[low]
                index = low
                break
              
        mid = (low+high)//2

        if nums[low]== nums[mid] and nums[mid]==nums[high]:
            low = low+1
            high = high -1
            continue

        if nums[low]<=nums[mid]:
            if nums[low]<ans:
                ans = nums[low]
                index = low
            low = mid +1

        else:
            if nums[mid]<ans:
                ans = nums[mid]
                index = mid
            high = mid-1
    return index

def main():
    nums = [4,5,5,6,7,1,2]
    result = how_many_times_array_rotared_with_duplicates(nums)
    print(result)
main()