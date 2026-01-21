class Solution:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

    @staticmethod
    def array_to_ll(arr):
        if not arr:
            return None
        head = Solution(arr[0])
        current = head

        for value in arr[1:]:
            current.next = Solution(value)
            current = current.next
        return head
    
    def brute(self,head):
        if head is None or head.next is None:
            return head
        
        arr = []
        temp = head
        while temp and temp.next:
            arr.append(temp.data)
            temp = temp.next.next
        if temp :
            arr.append(temp.data)

        temp = head.next
        while temp and temp.next:
            arr.append(temp.data)
            temp = temp.next.next
        if temp :
            arr.append(temp.data)

        i = 0
        temp = head
        while temp:
            temp.data = arr[i]
            i+=1
            temp = temp.next

        return head
    
    def optimal(self,head):
        if head is None or head.next is None:
            return head
        
        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next

            odd = odd.next
            even = even.next

        odd.next = evenHead
        return head 
    
    
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    head = Solution.array_to_ll(arr)
    sol = Solution(0)
    # brute = sol.brute(head)
    optimal = sol.optimal(head)
    # temp = brute
    temp = optimal


    while temp:
        print(temp.data,end=" -> ")
        temp = temp.next
    print("None")