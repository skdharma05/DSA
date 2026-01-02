class PalindromicSubstrings:
    def optimal(self, s):

        def check(left , right):
            count = 0
            while(left>=0 and right <len(s) and s[left] == s[right]):
                left -=1
                right+=1
                count+=1

            return count
        
        ans =0
        for i in range(len(s)):
            ans += check(i,i)
            ans += check(i,i+1)
        
        return ans
s = "babad" 
palindromicSubstrings=PalindromicSubstrings()
print(palindromicSubstrings.optimal(s))
