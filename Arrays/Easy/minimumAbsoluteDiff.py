class Solution:
    def optimal(self,arr):
        n = len(arr)
        arr.sort()
        min_diff = float('inf')
        res = []

        for i in range(n-1):
            diff = arr[i+1]-arr[i]
            if diff < min_diff:
                min_diff = diff
                res = [[arr[i],arr[i+1]]]
            elif diff == min_diff:
                res.append([arr[i],arr[i+1]])
        return res

if __name__ == "__main__":
    sol = Solution()
    arr = [4,2,1,3]
    print(sol.optimal(arr=arr))
