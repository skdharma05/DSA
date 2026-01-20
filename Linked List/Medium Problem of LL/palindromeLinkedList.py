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
    
    def better_using_stack(self,head): # Time Complexity = O(n)
        stack = []                      # Space Complexity = O(n/2)
        fast = head
        slow = head

        while fast and fast.next:
            stack.append(slow.data)
            slow = slow.next
            fast = fast.next.next

        if fast :
            slow = slow.next

        while slow:
            if stack.pop() != slow.data:
                return False
            slow = slow.next
            
        return True
    
    def optimal(self, head):  # Time Complexity = O(n) 
                              # Space Complexity = O(1)
        def reverse(head):
            if head is None or head.next is None:
                return head
            
            new_head = reverse(head.next)
            front  = head.next
            front.next = head
            head.next = None

            return new_head
        
        if head is None or head.next is None:
            return True 
        
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        new_head = reverse(slow.next)

        first = head
        second = new_head

        while second:
            if first.data != second.data:
                reverse(new_head)
                return False
            
            first = first.next
            second = second.next
        reverse(new_head)
        return True
        

if __name__ == "__main__":
    arr = [1,2,3,2,1]
    head = Solution.array_to_ll(arr)
    sol = Solution(0)
    print(sol.better_using_stack(head))
    print(sol.optimal(head))