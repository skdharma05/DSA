class NthRoot:
    def linea_search(self,n,m):
        for i in range(1,m+1):
            value = i **n
            if value==m:
                return i
            if value>m:
                break
        return -1
    
    def binary_search(self,n,m):
        if m ==0:
            return 0
        low =1
        high = m

        while low<=high:
            mid = (low+high)//2
            if mid**n ==m:
                return mid
            elif mid ** n >m:
                high = mid-1
            else:
                low = mid+1
        return -1
    
    def binary_search_for_longValue(self,n,m):
        #if we use big numbers like m = 100000 and n =10 this will make progeam slow and waste of memory.
        #solution for this.
        if m ==0:
            return 0
        low =1
        high = m

        while low<=high:
            mid = (low+high)//2
            val =1
            # for safely compute mid ** n
            for _ in range(n):
                val= val * mid
                if val >mid: # early stop 
                    break
                
            if val ==m:
                return mid
            elif val<mid:
                low = mid+1
            else :
                high = mid -1
        return -1
    

n =2
m = 8
nthRoot = NthRoot()
result = nthRoot.linea_search(n,m)
result2 = nthRoot.binary_search(n,m)
print (result2)