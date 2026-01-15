class Node:
    def __init__(self,data, next = None):
        self.data = data
        self.next = next
    @staticmethod
    def array_to_ll(arr):
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
        temp = head
        prev = None

        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
        return prev
    
    def usingRecursion(self, head):

        if head is None or head.next is None:
            return head
        
        newHead = self.usingRecursion(head.next)
        front = head.next
        front.next = head
        head.next = None
        return newHead

if __name__ == "__main__":
    arr=[1,2,3,4,5]
    head = Node.array_to_ll(arr)
    node = Node(0)
    # reverse = node.brute(head)
    # reverse = node.optimal(head)
    reverse = node.usingRecursion(head)
    while reverse :
        print(reverse.data)
        reverse = reverse.next
