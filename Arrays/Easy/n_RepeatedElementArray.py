class N_repeated_element_in_size_2N_array:
    def better(self,num):
        seen = set()

        for n in num:
            if n in seen:
                return n
            seen.add(n)
        return 0
    def optimal(self,num):
        n = len(num)
        for i in range(n-1):
            if num[i]==num[i+1]:
                return num[i]
            if i + 2 < n and num[i]==num[i+2]:
                return num[i]
            if i + 3 < n and num[i]==num[i+3]:
                return num[i]
        return 

nums = [1,2,3,3] 
solution = N_repeated_element_in_size_2N_array()
print(solution.better(nums))
print(solution.optimal(nums))