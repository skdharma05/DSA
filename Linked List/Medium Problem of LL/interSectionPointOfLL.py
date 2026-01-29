class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def brute_using_set(self, headA, headB):
        visited = set()
        
        temp = headA
        while temp:
            visited.add(temp)
            temp = temp.next

        temp = headB
        while temp:
            if temp in visited:
                return temp
            temp = temp.next
        return None
    
    def brute_using_map(self, headA, headB):
        visited = {}

        temp = headA
        while temp:
            visited[temp] = 1
            temp = temp.next

        temp = headB
        while temp:
            if temp in visited:
                return temp
            temp = temp.next
        return None
    
    def better(self, headA, headB):

        def collision(smallerHead,LongerHead,lengthDiff):

            temp1,temp2 = smallerHead,LongerHead
            for _ in range(lengthDiff):
                temp2 = temp2.next
            
            while temp1 != temp2:
                temp2 = temp2.next
                temp1 = temp1.next
            return temp1
        
        temp1 = headA
        n1 = 0
        temp2 = headB
        n2 = 0

        while temp1:
            n1 += 1
            temp1 = temp1.next
        
        while temp2:
            n2 += 1
            temp2 = temp2.next
        
        if n1 < n2:
            return collision(headA,headB,n2-n1)
        return collision(headB,headA,n1-n2)
    
    def optimal(self,headA,headB):
        if headA is None or headB is None:
            return None
        temp1 = headA
        temp2 = headB

        while temp1 != temp2:
            temp1 = temp1.next
            temp2 = temp2.next

            if temp1 == temp2:
                return temp1
            if temp1 is None:
                temp1 = headB 
            if temp2 is None:
                temp2 = headA

        return temp1

            
def insertNode(head, val):
    newNode = ListNode(val)
    
    if head is None:
        head = newNode
        return head
    
    temp = head
    while temp.next is not None:
        temp = temp.next
    
    temp.next = newNode
    return head

def printList(head):
    while head.next is not None:
        print(head.val, end="->")
        head = head.next
    print(head.val)

if __name__ == "__main__":
    # Creation of the first list
    head1 = ListNode()
    head1 = insertNode(head1, 1)
    head1 = insertNode(head1, 3)
    head1 = insertNode(head1, 1)
    head1 = insertNode(head1, 2)
    head1 = insertNode(head1, 4)

    # Create an intersection
    intersection = head1.next.next.next

    # Creation of the second list
    head2 = ListNode()
    head2 = insertNode(head2, 3)
    head2.next = intersection

    # Printing the lists
    print("List1: ", end="")
    printList(head1)
    print("List2: ", end="")
    printList(head2)

    # Checking if an intersection is present
    sol = Solution()
    # answerNode = sol.brute_using_set(head1, head2)
    # answerNode = sol.brute_using_map(head1, head2)
    # answerNode = sol.better(head1, head2)
    answerNode = sol.optimal(head1, head2)
    if answerNode is None:
        print("No intersection")
    else:
        print("The intersection point is", answerNode.val)
