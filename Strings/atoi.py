class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)
        result = 0
        sign = 1

        while i < n and s[i] == " ":
            i+=1

        if s[i] == '-':
            sign = -1
            i+=1
        elif sign == '+':
            i+=1

        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])

            if sign * result > 2**31-1:
                return 2**31-1
            elif sign * result < -2**31:
                return -2**31
            i+=1

        return sign * result

if __name__ == "__main__":
    a = "  -4321abc01"
    b = "  431a2b3"
    sol = Solution()
    print(sol.myAtoi(a))
    print(sol.myAtoi(b))
