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
    
    @staticmethod
    def insertHead(head,el):
        temp = Node(el)
        temp.next = head
        head.prev = temp
        
        return temp
       
    @staticmethod
    def insertTail(head,el):
        newEle = Node(el)

        if head is None:
            return newEle
        if head.next is None:
            head.next = newEle
            newEle.prev = head
            return head
        
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = newEle
        newEle.prev = temp
        return head
    
    @staticmethod
    def insertBeforeTail(head,el):
        newEle = Node(el)

        if head is None:
            return newEle
        
        if head.next is None:
            head.prev = newEle
            newEle.next = head
            return newEle
        
        temp = head
        while temp.next is not None:
            temp = temp.next

        prev = temp.prev
        temp.prev = newEle
        newEle.next = temp
        newEle.prev = prev
        prev.next = newEle
        
        return head
       
    @staticmethod
    def insertK(head,k,el):
        newNode = Node(el)
        if head is None:
            return newNode
        
        if k == 1:
            newNode.next = head
            head.prev = newNode
            return newNode

        temp = head
        count =  1
        while temp is not None and count < k-1 :
            temp = temp.next
            count+=1
        
        if temp is not None:
            front = temp.next
            newNode.next = front 
            newNode.prev = temp   
            temp.next = newNode
            if front:
                front.prev = newNode
        return head
       
    @staticmethod
    def insertElement(head,k,el):
        newNode = Node(el)
        if head.data == k:
            newNode.next = head
            head.prev = newNode
            return newNode

        temp = head
        while temp.next is not None :
            if temp.next.data == k:   
                front = temp.next
                newNode.next = front
                newNode.prev = temp
                front.prev= newNode
                temp.next = newNode
                break
            temp = temp.next
            
        return head
       
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    head = Node.array_to_linked_list(arr)
    # insert_head =Node.insertHead(head,4) 
    # insert_tail =Node.insertBeforeTail(head,6) 
    # insert_k =Node.insertK(head,el=9,k=6) 
    insert_value =Node.insertElement(head,3,el=8) 
    
    while insert_value:
        print(insert_value.data)
        insert_value = insert_value.next
    
