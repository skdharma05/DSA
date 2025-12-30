class LongestPalindromicSubstring:
    def optimal(self,s):
        if len(s)<2:
            return s
        start =0
        end =0
        def expandFromCenter(left,right):
            while left>=0 and right <len(s) and s[left]==s[right]:
                left -=1
                right +=1
            return left+1,right-1
        
        for i in range(len(s)):
            l1,r1 = expandFromCenter(i,i)
            l2,r2 = expandFromCenter(i,i+1)

            if r1 - l1 >end - start:
                start,end = l1,r1
            if r2 - l2 >end - start:
                start,end = l2,r2
        return s[start:end+1]

            

s = "babad" 
longestPalindromicSubstring=LongestPalindromicSubstring()
print(longestPalindromicSubstring.optimal(s))
