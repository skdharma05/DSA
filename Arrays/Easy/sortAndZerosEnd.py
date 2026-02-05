class Solution:
    def sort_Zeros_at_end(self,arr):
        non_zeros = []
        zeros = []
        for x in arr:
            if x != 0:
                non_zeros.append(x)
            else:
                zeros.append(x) 
        non_zeros.sort()
        
        return non_zeros + zeros

if __name__ == "__main__":
    sol = Solution()
    arr = [0,5,3,0,2,0,1,4]
    print(sol.sort_Zeros_at_end(arr))
