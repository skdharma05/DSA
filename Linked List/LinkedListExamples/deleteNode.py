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
    def deleteHead(head):
        if head is None:
            return head
        return head.next
       
    @staticmethod
    def deleteTail(head):
        if head is None or head.next == None:
            return None
        temp = head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None
        return head
       
    @staticmethod
    def deleteK(head,k):
        if head is None:
            return None
        if k == 1:
            head = head.next
            return head

        temp = head
        count =  1
        while temp.next is not None and count < k-1:
            temp = temp.next
            count+=1
        if temp.next:        
            temp.next =  temp.next.next
        return head
       
    @staticmethod
    def deleteElement(head,k):
        if head is None:
            return None
        
        if head.data == k:
            return head.next

        temp = head
        while temp.next is not None :
            if temp.next.data == k:   
                temp.next = temp.next.next
                break
            temp = temp.next
        return head
       
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    head = Node.array_to_linked_list(arr)
    # delete_head =Node.deleteHead(head) 
    # delete_tail =Node.deleteTail(head) 
    # delete_k =Node.deleteK(head,3) 
    delete_k =Node.deleteElement(head,3) 
    # while delete_head:
    #     print(delete_head.data)
    #     delete_head = delete_head.next
    while delete_k:
        print(delete_k.data)
        delete_k = delete_k.next

