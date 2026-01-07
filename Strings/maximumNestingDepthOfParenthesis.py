class Solution :
    def maximumNestingDepthOfParenthesis(self,s):
        count=0
        result =0
        for ch in s:
            if ch == '(':
                count +=1
                if result < count:
                    result = count
            elif ch ==')':
                count-=1
        return result

s = "(1+(2*3)+((8)/4))+1"
sol = Solution()
print(sol.maximumNestingDepthOfParenthesis(s))