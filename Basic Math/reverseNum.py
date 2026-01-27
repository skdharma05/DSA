class Solution:
    def reverseNum(self,n):
        revNum = 0

        while n > 0:
            lastDigit = n % 10

            revNum = revNum * 10 + lastDigit

            n = n//10 # remove n th last digit
    
        return revNum

if __name__ == "__main__":
    sol = Solution()
    n = 12345
    print(sol.reverseNum(n))