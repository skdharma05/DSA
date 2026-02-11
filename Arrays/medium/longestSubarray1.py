class Solution:
    def subarray(self, arr):
        n = len(arr)
        max_len = 0
        for i in range(n):
            odd = set()
            even = set()
            for j in range(i, n):
                if arr[j] % 2 == 1:
                    odd.add(arr[j])
                else:
                    even.add(arr[j])
            if len(odd) == len(even):
                max_len = max(max_len, j-i+1)

        return max_len

if __name__ == "__main__":
    sol = Solution()
    arr = [1,2,3,2]
    print(sol.subarray(arr))