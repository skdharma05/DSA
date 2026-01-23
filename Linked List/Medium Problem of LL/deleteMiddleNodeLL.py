class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

    @staticmethod
    def array_to_linked_list(arr):
        if not arr:
            return None
        
        head = Node(arr[0])
        current = head

        for value in arr[1:]:
            current.next = Node(value)
            current = current.next

        return head
    
    def brute(self,head):
        temp = head
        cnt =0
        while temp is not None:
            cnt+=1
            temp = temp.next
        
        middleNode = (cnt // 2)
        temp = head 

        while temp:
            middleNode -=1
            if middleNode == 0:
                break
            temp = temp.next
        temp.next = temp.next.next
        return head
    
    def optimal(self,head):
        if head is None or head.next is None:
            return None
        
        slow = head
        fast = head
        fast = fast.next.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        slow.next = slow.next.next
        return head


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    head = Node.array_to_linked_list(arr)
    node = Node(0)
    # brute = node.brute(head)
    optimal = node.optimal(head)
    
    temp = optimal
    while temp:
        print(temp.data , end=' -> ')
        temp = temp.next
    print('None')

    
