class Kth_missing_number:
    def optimal(self,arr,k):
        n = len(arr)
        low = 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            missing =  arr[mid]-(mid+1)
            if missing<k:
                low = mid +1
            else:
                high = mid -1
        return high+1+k



arr = [2,3,4,7,11]
k=3
missing_num = Kth_missing_number()
print(missing_num.optimal(arr,k))