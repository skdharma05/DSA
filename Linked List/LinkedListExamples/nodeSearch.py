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
    
    @staticmethod
    def searchNode(head,value):
        temp = head
        while temp:
            if temp.data == value:
                return True
            temp = temp.next
        return False
    
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    head = Node.array_to_linked_list(arr)
    print(Node.searchNode(head,4))


