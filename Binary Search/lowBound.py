def lowBound(nums, k):
        n = len(nums)
        low =0
        high = n -1
        ans = n

        while low<=high:
            mid = (low+high)//2
            if nums[mid]>=k:
                  ans = mid
                  high = mid -1
            else:
                  low = mid +1
        
        return ans
def main():
     num = [-1,0,3,5,9,12]
     result = lowBound(num,9)
     print(result)
main()