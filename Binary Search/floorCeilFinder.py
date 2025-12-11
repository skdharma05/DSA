def findFloor(nums,k):
    n = len(nums)
    low = 0
    high =n-1
    ans =-1
    while low<=high:
        mid = (high + low)//2
        if nums[mid]<=k:
            ans = nums[mid]
            low = mid +1
        else :
            high = mid -1
    return ans

def findCeil(nums,k):
    n = len(nums)
    low = 0
    high =n-1
    ans =-1
    while low<=high:
        mid = (high + low)//2
        if nums[mid]>=k:
            ans = nums[mid]
            high = mid -1
        else :
            low = mid +1

    return ans


def get_floor_and_ceil(nums,k):
    floor = findFloor(nums,k)
    ceil = findCeil(nums,k)
    return floor , ceil

def main():
    num = [3, 4, 4, 7, 8, 10]
    result = get_floor_and_ceil(num,9)
    print(result)
main()