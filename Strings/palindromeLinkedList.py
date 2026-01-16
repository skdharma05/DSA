class Solution:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

    @staticmethod
    def arrayTtoLL(arr):
        if not arr:
            return None
        head = Solution(arr[0])
        current = head

        for value in arr[1:]:
            current.next = Solution(value)
            current = current.next
        return head
    
    def optimal_using_stack(self,head): # Time Complexity = O(n)
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

if __name__ == "__main__":
    arr = [1,2,3,2,1]
    head = Solution.arrayTtoLL(arr)
    sol = Solution(0)
    print(sol.optimal_using_stack(head))