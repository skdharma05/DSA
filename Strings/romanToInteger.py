class Solution:
    def romanToInteger(self,s):
        roman = {
            'I'  :  1,
            'V'  :  5,
            'X'  :  10,
            'L'  :  50,
            'C'  :  100,
            'D'  :  500,
            'M'  :  1000
        }

        prev = 0
        total =0

        for ch in range(len(s)-1,-1,-1):
            current = roman[s[ch]]
            
            if current >= prev:
                total += current
            else:
                total -= current
            prev = current
        
        return total
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.romanToInteger("III"))     
    print(sol.romanToInteger("IV"))      
    print(sol.romanToInteger("MCMIV"))   



            
