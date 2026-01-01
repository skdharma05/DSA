import heapq

class MinimiseMaximumDistanceBetweenGasStations:
    def brute(self, arr, k):
        n= len(arr)
        how_many = [0]*(n-1)

        for _ in range(k):
            max_section = -1
            max_ind = -1

            for i in range( n-1):
                diff = arr[i+1]-arr[i]
                section_length = diff /(how_many[i]+1)
                if section_length>max_section:
                    max_section = section_length
                    max_ind = i

            how_many[max_ind]+=1
        max_ans = -1
        for i in range(n-1):
            diff = arr[i+1]-arr[i]
            section_length = diff /(how_many[i]+1)
            max_ans = max(max_ans,section_length)
        
        return max_ans
    

    def better(sef,arr,k):
        n = len(arr)
        how_many = [0]*(n-1)

        pq =[]
        for i in range(n-1):
            dist = arr[i+1]- arr[i]
            heapq.heappush(pq,(-dist,i))
        
        for _ in range(k):
            negDist , idx = heapq.heappop(pq)
            how_many[idx]+=1
            total_dist = arr[idx+1]- arr[idx]
            newDist = total_dist /(how_many[idx]+1)
            heapq.heappush(-negDist,idx)

        return pq[0][0]
    

arr = [1, 2, 3, 4, 5]
k = 4

minimiseMaximumDistanceBetweenGasStations = MinimiseMaximumDistanceBetweenGasStations()
print(minimiseMaximumDistanceBetweenGasStations.brute(arr,k))