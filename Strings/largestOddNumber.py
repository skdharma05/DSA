class LargesOddNumber:
    def optimal(self , num):
        n = len(num)
        for i in range(n-1,-1,-1):
            if int(num[i]) % 2 == 1:
                return num[:i+1]
        return ""

num = '52'
num2= '3472'
solution = LargesOddNumber()
print(solution.optimal(num))
print(solution.optimal(num2))