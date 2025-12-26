class ShipWithinDays:
    def brute(self,weights,days):
        left = max(weights)
        right = sum(weights)

        for capacity in range(left , right+1):
            need_days =1
            current_load =0

            for weight in weights:
                if current_load + weight <=capacity:
                    current_load+=weight
                else:
                    need_days+=1
                    current_load =weight
            if need_days<=days:
                return capacity

    def optimal(self,weights,days):
        low = max(weights)
        high = sum(weights)
        ans = -1
        while low<=high:
            mid = (low+high)//2
            need_days =1
            load =0
            for weight in weights:
                if load + weight<=mid:
                    load +=weight
                else:
                    need_days +=1
                    load = weight
            if need_days<=days:
                ans = mid
                high = mid-1
            else:
                low = mid +1
        return ans



weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
shipWithinDays = ShipWithinDays()
print(shipWithinDays.brute(weights,days))
print(f"The ship capacity is : {shipWithinDays.optimal(weights,days)}")