
# def longestSubarray( nums, k):
        # prefixSum = 0
        # maxLength = 0
        # prefixIndexMap = {}  # dictionary to store prefixSum first index

        # for i in range(len(nums)):
        #     prefixSum += nums[i]

        #     # Case 1: whole array from 0...i has sum k
        #     if prefixSum == k:
        #         maxLength = max(maxLength, i + 1)

        #     # Case 2: check if prefixSum - k seen before
        #     if (prefixSum - k) in prefixIndexMap:
        #         length = i - prefixIndexMap[prefixSum - k]
        #         maxLength = max(maxLength, length)

        #     # Store prefixSum only if not present (first occurrence)
        #     if prefixSum not in prefixIndexMap:
        #         prefixIndexMap[prefixSum] = i

        # return maxLength

def longestSubarray(nums, k):
    n = len(nums)
    left = 0
    sum = 0
    maxLen = 0
    right =0

    # for right in range(n):        # expand window by moving right
    #     sum += nums[right]        # add current element to sum

    #     while sum > k:            # sum too big? shrink from left
    #         sum -= nums[left]
    #         left += 1

    #     if sum == k:              # check if equal
    #          maxLen = max(maxLen, right - left + 1)

    while right < n:
        while left<right and sum>k:
            sum = sum - nums[left]
            left+=1
        
        if sum == k:
            maxLen = max(maxLen,right-left+1)
        
        right+=1
        if right<n:
            sum = sum + nums[right]



    return maxLen


def main():
     num = [2,1,1,1,3,2]

     result = longestSubarray(num,k=3)
     print(result)

main()
