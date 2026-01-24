class Solution:
    def optimal(self,nums):
        nums.sort()
        max_sum = 0
        for i in range(len(nums)//2):
            current_sum = nums[i] + nums[len(nums)-1-i] # 1 index + last index
            max_sum =  max(max_sum,current_sum )
        return max_sum

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    sol = Solution()
    print(sol.optimal(arr))

