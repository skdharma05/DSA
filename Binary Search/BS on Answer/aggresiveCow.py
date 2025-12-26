# Leetcode 1552 as Magnetic force between two balls same as Aggressive Cow.

class AggressiveCow:
    def brute(self,stalls,k):
        stalls.sort()

        def canPlaced(dist):
            n = len(stalls)
            count =1
            last = stalls[0]
            for i in range(1,n):
                if stalls[i] - last >= dist:
                    count +=1
                    last = stalls[i]
                if count>=k:
                    return True
            return False

        max_dist = stalls[-1] - stalls[0]
        ans = 0
        for dist in range(1, max_dist + 1):
            if canPlaced(dist):
                ans = dist
            else:
                break
        return ans

    
    def optimal(self,stalls,k):
        stalls.sort()

        def canPlaced(dist):
            n = len(stalls)
            count =1
            last = stalls[0]
            for i in range(1,n):
                if stalls[i] - last >= dist:
                    count +=1
                    last = stalls[i]
                if count>=k:
                    return True
            return False

        low =1
        high = stalls[-1] - stalls[0]
        ans = 0
        while low<=high:
            mid = (low+high)//2
            if canPlaced(mid):
                ans = mid
                low = mid+1
            else:
                high = mid-1
        return ans
    
k = 4
stalls = [0, 3, 4, 7, 10, 9]
aggressive_Cow= AggressiveCow()
print(aggressive_Cow.brute(stalls,k))
print(aggressive_Cow.optimal(stalls,k))

