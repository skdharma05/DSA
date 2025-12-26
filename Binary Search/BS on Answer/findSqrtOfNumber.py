class SqureRoot:
    def using_linear_search(self,num):
        n = num
        ans =1
        for i in range(n):
            if i*i <= n :
                ans = i
            else:
                break
        return ans
    
    def using_binary_search(self,n):
        low = 1
        high = n
        ans =0

        while low<=high:
            mid = (low + high) //2
            if mid * mid <= n:
                ans =  mid
                low = mid +1
            else:
                high = mid -1
        
        return ans

num =28
linear = SqureRoot()
result = linear.using_linear_search(num)
result2 = linear.using_binary_search(num)
print ( result\
       ,result2)