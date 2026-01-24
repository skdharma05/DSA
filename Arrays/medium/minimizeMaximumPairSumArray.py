class Solution:
    def optimal(self,nums):
        nums.sort()
        max_sum = 0
        for i in range(len(nums)//2):
            current_sum = nums[i] + nums[len(nums)-1-i] # 1 index + last index
            max_sum =  max(max_sum,current_sum )
        return max_sum
    
    def optimal2(self,nums):
        sorted_array = sorted(nums)

        left = 0
        right = len(nums)-1
        max_sum = 0

        while left < right:
            maxi = sorted_array[left] + sorted_array[right]
            max_sum = max(max_sum,maxi)
            left+=1
            right-=1
        return max_sum


if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    sol = Solution()
    print(sol.optimal(arr))
    print(sol.optimal2(arr))

