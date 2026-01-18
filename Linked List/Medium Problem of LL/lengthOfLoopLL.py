
class Solution:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

    def brute_using_map(self,head):
        nodeMap = {}
        temp = head
        timer = 1
        while temp:
            if temp in nodeMap:
                value = nodeMap[temp]
                return timer - value
            nodeMap[temp] = timer
            timer+=1
            temp = temp.next
        return 0
    
    def optimal(self,head):  #   Floyd's Cycle Detection Algorithm "Tortoise and Hare Algorithm"
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cnt = 1
                slow = slow.next
                while slow != fast:
                    cnt+=1
                    slow = slow.next
                return cnt
        return 0

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
