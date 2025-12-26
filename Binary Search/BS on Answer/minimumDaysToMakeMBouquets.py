class Minimum_days_to_make_m_bouquets:

    def brute(self,bloomDay,m,k):
        n = len(bloomDay)
        if n <m*k:
            return -1
        
        min_day = min(bloomDay)
        max_day = max(bloomDay)
        for day in range(min_day,max_day+1):
            bouquets =0
            flower_cnt =0
            for bloom in bloomDay:
                if bloom<=day:
                    flower_cnt+=1
                    if flower_cnt == k:
                        bouquets+=1
                        flower_cnt =0
                else:
                    flower_cnt=0
            if bouquets >=m:
                return day
        
        return -1
    
    # Using Binary search.
    def optimal(self,bloomDay,m,n):
        n = len(bloomDay)
        if n <m*k:
            return -1
        
        low = min(bloomDay)
        high = max(bloomDay)
        ans =-1

        while low <= high:
            mid = (low + high)//2
            flower =0
            bouquets = 0

            for bloom in bloomDay:
                if bloom <=mid:
                    flower += 1
                    if flower == k:
                        bouquets +=1
                        flower =0
                else:
                    flower =0

            if bouquets >=m:
                ans = mid
                high = mid -1
            else:
                low = mid +1

        return ans



bloomDay =[7,7,7,7,13,11,12,7]
m = 2 
k =3
solution = Minimum_days_to_make_m_bouquets()
print(solution.brute(bloomDay,m,k))
print(solution.optimal(bloomDay,m,k))
        