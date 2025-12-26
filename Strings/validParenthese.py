class ValidPraenthese:
    def optimal(self,strs):

        stack = []
        match = {')':'(','}':'{',']':'['}

        for ch in strs:
            if ch in match.values():
                stack.append(ch)
            else:
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()
        
        return len(stack)==0

        

strs1 = "()"
strs2="(]"
strs3="([])"
strs4="({)}"

valid_praenthese = ValidPraenthese()
print(valid_praenthese.optimal(strs1))
print(valid_praenthese.optimal(strs2))
print(valid_praenthese.optimal(strs3))
print(valid_praenthese.optimal(strs4))
