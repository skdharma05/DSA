class Solution:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    
    @staticmethod
    def arrayToLL(arr):
        if not arr:
            return None
        
        head =Solution(arr[0])
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
        while temp:
            arr.append(temp.data)
            temp = temp.next

        arr.sort()
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
        
        def findMiddle(head):
            if head is None or head.next is None:
                return head
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def mergeTwoSortedLinkedLists(list1, list2):
        # Create a dummy node
            dummyNode = Solution(0)
            
            # Temp pointer to build merged list
            temp = dummyNode

            # Traverse both lists
            while list1 and list2:
                # Choose smaller node
                if list1.data <= list2.data:
                    temp.next = list1
                    list1 = list1.next
                else:
                    temp.next = list2
                    list2 = list2.next
                # Move temp pointer
                temp = temp.next
            temp.next = list1 if list1 else list2
            return dummyNode.next

        middle = findMiddle(head)

        # Split into two halves
        right = middle.next
        middle.next = None
        left = head

        # Recursively sort both halves
        left = self.optimal(left)
        right = self.optimal(right)

        # Merge sorted halves
        return mergeTwoSortedLinkedLists(left, right)


if __name__ == "__main__":
    arr = [3,5,1,8,4,2,9]
    # arr = []
    head = Solution.arrayToLL(arr)
    sol = Solution(0)
    # brute  = sol.brute(head)
    optimal  = sol.optimal(head)

    temp = optimal

    while temp:
        print(temp.data , end=' -> ')
        temp = temp.next
    print(None)
        