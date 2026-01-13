class Node:
    def __init__(self,data,next = None,prev = None):
        self.data = data
        self.prev = prev
        self.next = next

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
    
if __name__ == '__main__':
    arr= [1,2,3,4,5,6]
    head = Node.array_to_linked_list(arr=arr)
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next