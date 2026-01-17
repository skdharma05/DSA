class Solution:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    def brute_using_map(self,head):
        nodeMap = {}
        temp = head
        while temp:
            if temp in nodeMap:
                return temp.data
            nodeMap[temp] = 1
            temp = temp.next
        return None
    
    def optimal(self,head): #Floyd's Cycle Detection Algorithm "Tortoise and Hare Algorithm"
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow.data
        return None

if __name__ == "__main__":
    head = Solution(1)
    second = Solution(2)
    third = Solution(3)
    fourth = Solution(4)
    fifth = Solution(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = third

    sol = Solution(0)
    print(sol.brute_using_map(head))
    print(sol.optimal(head))
