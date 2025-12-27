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

            
        
arr1 = [2, 4, 6]
arr2 = [1, 3, 5]
median = Median_of_two_sorted_array()
print(median.brute(arr1,arr2))
print(median.better(arr1,arr2))

