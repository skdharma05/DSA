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
    def insertHead(head,el):
        temp = Node(el)
        temp.next = head
        
        return temp
       
    @staticmethod
    def insertTail(head,el):
        newEle = Node(el)

        if head is None:
            return newEle
        
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = newEle
        return head
       
    @staticmethod
    def insertK(head,k,el):
        newNode = Node(el)
        if head is None:
            return newNode
        if k == 1:
            temp = newNode
            temp.next = head
            return temp

        temp = head
        count =  1
        while temp.next is not None and count < k-1:
            temp = temp.next
            count+=1
        if temp.next is not None:  
            newNode.next = temp.next      
            temp.next =  newNode
        return head
       
    @staticmethod
    def insertElement(head,k,el):
        newNode = Node(el)
        if head.data == k:
            temp = newNode
            temp.next = head
            return temp

        temp = head
        while temp.next is not None :
            if temp.next.data == k:   
                newNode.next = temp.next
                temp.next = newNode
                break
            temp = temp.next
        return head
       
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    head = Node.array_to_linked_list(arr)
    # insert_head =Node.insertHead(head,4) 
    # insert_tail =Node.insertTail(head,6) 
    # insert_k =Node.insertK(head,el=9,k=3) 
    insert_value =Node.insertElement(head,3,el=8) 
    
    while insert_value:
        print(insert_value.data)
        insert_value = insert_value.next
    
