class Median_of_two_sorted_array:
    def brute(self,num1,num2):
        n1 = len(num1)
        n2 = len(num2)

        i=0
        j=0
        num3=[]

        while i<n1 and j <n2:
            if num1[i]<num2[j]:
                num3.append(num1[i])
                i+=1
            else:
                num3.append(num2[j])
                j+=1

        while i<n1:
            num3.append(num1[i])
            i+=1
        while j<n2:
            num3.append(num2[j])
            j+=1

        n = len(num3)
        if n % 2 ==1:
            return num3[n//2]
        else:
            return (num3[n//2]+ num3[n//2-1])/2.0
        

    def better(sef,num1,num2):
        n1 = len(num1)
        n2 = len(num2)
        n = n1+n2

        i=0
        j=0
        count =0

        ind2=  n//2
        ind1 = ind2-1

        ind1el = -1
        ind2el = -1

        while i<n1 and j <n2:
            if num1[i]<num2[j]:
                if count == ind1:
                    ind1el = num1[i]
                if count == ind2:
                    ind2el = num1[i]
                i+=1
            
            else:
                if count == ind1:
                    ind1el = num2[j]
                if count == ind2:
                    ind2el = num2[j]
                j+=1

            count +=1
        while i <n1:
            if count == ind1:
                ind1el = num1[i]
            if count == ind2:
                ind2el = num1[i]
            i+=1
            count +=1
        while j<n2:
            if count == ind1:
                    ind1el = num2[j]
            if count == ind2:
                    ind2el = num2[j]
            j+=1
            count+=1
        
        if n%2 ==1:
            return float(ind2el)
        else:
            return (ind1el+ind2el)/2.0
        

    def optimal(self, nums1,nums2):
        n1 = len(nums1)
        n2 = len(nums2)

        if len(nums1)>len(nums2):
            return self.optimal(nums2,nums1)
        
        n = n1+ n2
        left = (n1 + n2 + 1) //2

        low = 0
        high = n1

        while low <= high:
            mid1 = (low+ high)//2
            mid2 = left - mid1
            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')

            if mid1 > 0:
                l1 = nums1[mid1-1]
            if mid2 > 0:
                l2 = nums2[mid2-1]
            if mid1 <n1:
                r1 = nums1[mid1]
            if mid2 <n2:
                r2 = nums2[mid2]

            if l1<=r2 and l2 <= r1:
                if n% 2 ==1:
                    return max(l1,l2)
                else:
                    return (max(l1,l2)+ min(r1,r2))/2.0
            elif l1>r2:
                high = mid1 -1
            else:
                low = mid1 +1
        return 0

        
arr1 = [2, 4, 6]
arr2 = [1, 3, 5]
median = Median_of_two_sorted_array()
print(median.brute(arr1,arr2))
print(median.better(arr1,arr2))
print(median.optimal(arr1,arr2))

