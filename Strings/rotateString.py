class RotateString:
    def optimal(self,s,target):
        if len(s) != len(target):
            return False
        combineStr = s + s
        if target in combineStr:
            return True
        return False

s = "abcde"
goal = "cdeab" 

s2 = "abcde",
goal2 = "abced"
solution = RotateString()
print(solution.optimal(s,goal))
print(solution.optimal(s2,goal2))