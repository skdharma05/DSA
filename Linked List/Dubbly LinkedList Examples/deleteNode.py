class Node:
    def __init__(self,data,prev = None, next = None):
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
            new_node = Node(value)
            current.next = new_node
            new_node.prev = current
            current = new_node
        return head
    
    @staticmethod
    def deleteHead(head):
        if head is None:
            return None
        
        newhead = head.next

        if newhead is not None:
            newhead.prev = None
        head.next = None

        return newhead
    
    @staticmethod
    def deleteTail(head):
        if head is None or head.next is None:
            return None
        temp = head
        while temp.next is not None:
            temp = temp.next

        prevNode = temp.prev
        prevNode.next = None
        temp.prev = None

        return head

    
if __name__ == '__main__':
    arr= [1,2,3,4,5,6]
    head = Node.array_to_linked_list(arr=arr)
    # delete_head = Node.deleteHead(head)
    delete_tail= Node.deleteTail(head)

    while delete_tail:
        print(delete_tail.data)
        delete_tail = delete_tail.next