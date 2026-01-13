
class Node:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.next = next
        self.prev = prev

    @staticmethod
    def array_to_linked_list(arr):
        if not arr:
            return None
        
        head = Node(arr[0])
        current = head

        for value in arr[1:]:
            newValue = Node(value)
            current.next = newValue
            newValue.prev = current
            current = newValue

        return head
    
    def brute(self,head):
        temp = head
        stack = []
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next
        
        temp = head
        while temp is not None:
            temp.data = stack[-1]
            stack.pop()
            temp = temp.next
        return head
    def optimal(self,head):
        if  head is None or head.next is None:
            return head
        prev = None
        current = head
        while current is not None:          # swap
            last = current.prev             # temp = a
            current.prev = current.next     # a = b
            current.next = last             # b = temp
                                            
            newHead = current
            current = current.prev
            
        return newHead


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    head = Node.array_to_linked_list(arr)
    node = Node(0)
    # brut = node.brute(head=head)
    optimal = node.optimal(head)
    while optimal:
        print(optimal.data)
        optimal = optimal.next 

