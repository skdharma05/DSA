class Solution:
    def brute(self,arr):
        sumi = {}
        cnt = {}

        for index , value in enumerate(arr):
            sumi[value] = sumi.get(value,0)+index
            cnt[value] = cnt.get(value,0)+1
        
        result = {}
        for value in sumi:
            if cnt[value] > 1:
                result[value] = sumi[value]

        return result

if __name__ == "__main__":
    sol = Solution()
    arr = [1,2,3,4,2,1,5,3]
    print(sol.brute(arr=arr))