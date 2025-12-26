class Koko_eating_bananas:
    def brute(self,nums,hr):
        n= max(nums)
        for i in range(1,n+1):
            hours =0
            for num in nums:
                hours = hours +(num + i-1)//i

            if hours <=hr:
                return i
    
    def totalHours(self,piles,speed):
        hours = 0
        for pile in piles:
            hours = hours+(pile+speed-1)//speed
            if hours>hr:
                break
        return hours
    def optimal(self,piles,hr): # Using Recrussion.
        low =1
        high = max(piles)
        ans = high
        while low<=high:
            mid = (low+high)//2
            hours = self.totalHours(piles,mid) #call Function using Recrussive method.
            if hours<=hr:
                ans = mid 
                high = mid -1
            else :
                low = mid +1
        return ans

    def optimal2(self,piles,hr): #without Recrussion
        low =1
        high = max(piles)
        ans = high
        while low<=high:
            mid = (low+high)//2
            hours = 0
            for pile in piles:
                hours = hours + (pile + mid -1)//mid
                if hours >hr:
                    break
            if hours<=hr:
                ans = mid 
                high = mid -1
            else :
                low = mid +1
        return ans

nums = [3,6,7,11]
hr =8
koko_eating_bananas = Koko_eating_bananas()
brute_result = koko_eating_bananas.brute(nums,hr) 
optimal_result = koko_eating_bananas.optimal(nums,hr) 
optimal2_result = koko_eating_bananas.optimal2(nums,hr) 
print(brute_result)
print(optimal_result)
print(optimal2_result)