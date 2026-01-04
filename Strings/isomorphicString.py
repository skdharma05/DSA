class IsomorphicString:
    def Optimal(self,s,t):
        n = len(s)
        m1= [0]*256
        m2= [0]*256

        for i in range(n):
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False
            
            m1[ord(s[i])] = i+1
            m2[ord(t[i])] = i+1
        
        return True

s = 'egg'
t = 'add'
solution = IsomorphicString()
print(solution.Optimal(s,t))