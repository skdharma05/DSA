class Node():
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    
    @staticmethod
    def arrToLL(arr):
        if not arr:
            return None
        head = Node(arr[0])
        current = head

        for value in arr[1:]:
            current.next = Node(value)
            current = current.next
        
        return head
    
    def brute(self,head):
        def reverseLL(head):
            temp = head
            prev = None

            while temp:
                front = temp.next
                temp.next = prev
                prev = temp
                temp = front
            return prev
        head = reverseLL(head)
        temp = head
        carry = 1
        while temp:
            temp.data = temp.data + carry
            if temp.data < 10:
                carry = 0
                break
            else:
                temp.data = 0
                carry = 1
            temp = temp.next
        
        if carry == 1:
            newNode = Node(1)
            head = reverseLL(head)
            newNode.next = head
            return newNode
        head = reverseLL(head)
        return head
    
    def optimal_using_recursion(self,head):
        def helper(temp):
            if temp is None:
                return 1
            carry = helper(temp.next)
            temp.data = temp.data + carry

            if temp.data < 10:
                return 0
            
            temp.data = 0
            return 1
        
        carry = helper(head)
        if carry:
            new_node = Node(carry)
            new_node.next = head
            return new_node
        
        return head

if __name__ == "__main__":
    arr = [1,5,9]
    head = Node.arrToLL(arr=arr)

    sol = Node(0)
    # brute = sol.brute(head) 
    optimal = sol.optimal_using_recursion(head)

    temp = optimal
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print('None')