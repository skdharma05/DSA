class Solution:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

    @staticmethod
    def arrToLL(arr):
        if not arr:
            return None
        head = Solution(arr[0])
        current = head

        for value in arr[1:]:
            current.next = Solution(value)
            current = current.next
        return head
    
    def optimal(self, l1 , l2):
        dummy = Solution(0)
        temp = dummy
        carry = 0

        while (l1 or l2) or carry:
            sum_val = 0
            if l1:
                sum_val += l1.data
                l1 = l1.next
            if l2:
                sum_val += l2.data
                l2 = l2.next
            
            sum_val += carry
            carry = sum_val // 10
            node = Solution(sum_val % 10)
            temp.next = node
            temp = temp.next
            
        return dummy.next
    

if __name__ == "__main__":
    arr1 = [2,4,3]        
    arr2 = [5,6,4]
    head1 = Solution.arrToLL(arr1)        
    head2 = Solution.arrToLL(arr2)     

    sol = Solution(0)
    optimal = sol.optimal(head1,head2)

    temp = optimal
    while temp:
        print(temp.data , end=' -> ')
        temp = temp.next
    print('None')   
