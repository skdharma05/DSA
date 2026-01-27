class Solution:
    def check_prime(self,n):
        if n < 2 :
            return False
        for i in range(2,n):
            if n % i == 0:
                return False
        return True
            
                  
if __name__ == "__main__":
    sol = Solution()
    n =7
    print(sol.check_prime(n))