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

    def brute(self,head,n):
        if head is None:
            return None
        
        cnt = 0
        temp = head
        while temp:
            cnt+=1
            temp = temp.next
        
        if cnt == n:
            return head.next
        res = cnt-n
        temp = head

        while temp :
            res-=1
            if res == 0:
                break
            temp = temp.next
        temp.next = temp.next.next

        return head
    
    def optimal(self,head,n):
        if head is None:
            return 
        
        dummy = Solution(0,head)
        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next
    


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    head = Solution.array_to_ll(arr)
    sol = Solution(0)
    # brute = sol.brute(head,2)
    optimal = sol.optimal(head,2)

    temp = optimal
    while temp:
        print(temp.data,end=" -> ")
        temp = temp.next
    print("None")