class Solution:
    def optimal(self,nums,k):
        nums.sort()
        result = float('inf')
        for i in range(len(nums) - k + 1):
            window = nums[i + k - 1] - nums[i]
            result = min(result, window)
        return result
if __name__ == "__main__":
    sol = Solution()
    nums = [9,4,1,7]
    k = 2
    print(sol.optimal(nums,k))  # Output: 2
