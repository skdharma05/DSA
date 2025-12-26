import re
class Palindrome:

    def brute(self,s):
        s = re.sub(r'[^a-zA-Z0-9]',"",s).lower()
        s_rev = s[::-1]
        if s != s_rev:
            return False
        return True
    
    def optimal(self,s):
        left = 0
        right = len(s)-1

        while left<right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            else:
                left +=1
                right -=1
        return True
    
    
s="A man, a plan, a canal: Panama"
palindrome = Palindrome()
print(palindrome.brute(s))
print(palindrome.optimal(s))