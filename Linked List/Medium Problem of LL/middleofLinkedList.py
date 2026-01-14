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
    
    def middleLinkedList_brute(self,head):
        temp = head
        cnt =0
        while temp is not None:
            cnt+=1
            temp = temp.next
        
        middleNode = (cnt // 2) + 1
        temp = head 
        while temp is not None:
            middleNode -=1
            if middleNode == 0:
                break
            temp = temp.next
        
        return temp
    
    def middleLinkedList_optimal(self,head):
        slow = head
        fast = head
        
        while fast.next is not None and fast is not None:

            fast = fast.next.next # move 2 steps
            slow = slow.next # move 1 step 

        return slow


if __name__ == "__main__":
    arr = [1,2,3,4,5]
    head = Node.array_to_linked_list(arr)
    node = Node(0)
    brute = node.middleLinkedList_brute(head)
    print(brute.data)
    optimal = node.middleLinkedList_optimal(head)
    print(optimal.data)

