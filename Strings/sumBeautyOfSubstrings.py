class Solution(object):
    def beautySum(self, s):
        n = len(s)
        total = 0
        for i in range(n):
            freq = {}
            for j in range(i,n):
                ch = s[j]
                freq[ch] = freq.get(ch,0)+1
                value = freq.values()
                maxi = max(value)
                mini = min(value)
                total+= (maxi - mini)
        return total
    
if __name__ == "__main__":
    sol = Solution()
    s = 'aabcb'
    print(sol.beautySum(s))

