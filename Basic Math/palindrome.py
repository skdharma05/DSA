class Solution:
    def isPalindrome(self,n):
        copy = n
        revNum = 0

        while n > 0:
            last_digit = n % 10
            revNum = revNum * 10 + last_digit
            n = n //10
        if revNum == copy:
            return True
        else:
            return False

        
if __name__ == "__main__":
    sol = Solution()
    n =123
    print(sol.isPalindrome(n))