class Solution:
    def amstrongSum(self,n):
        copy = n
        total = 0
        digit  = len(str(n))

        while n > 0:
            last_digit = n % 10
            total += last_digit ** digit
            n = n //10
        if total == copy:
            return True
        else:
            return False

        
if __name__ == "__main__":
    sol = Solution()
    n =153
    print(sol.amstrongSum(n))