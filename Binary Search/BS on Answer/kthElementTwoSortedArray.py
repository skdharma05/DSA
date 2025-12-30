class Kth_element_two_sorted_array:
    def optimal(self,nums1,nums2,k):
        n1 = len(nums1)
        n2 = len(nums2)
        if n1>n2:
            return self.optimal(nums2,nums1,k)
        low = max(k-n2,0)
        high = min(k,n1)
        left = k

        while low <= high:
            mid1 = (low + high )//2
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
                    return max(l1,l2)
            elif l1>r2:
                high = mid1 -1
            else:
                low = mid1 +1
        return 0

a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5

kth_element_two_sorted_array   = Kth_element_two_sorted_array()
print(kth_element_two_sorted_array.optimal(nums1= a,nums2= b, k=k))               

