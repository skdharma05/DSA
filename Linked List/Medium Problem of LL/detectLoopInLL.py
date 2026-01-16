class Solution:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

    # @staticmethod
    # def arrayToNode(arr):
    #     head = Solution(arr[0])
    #     current = head
    #     for value in arr[1:]:
    #         current.next = Solution(value)
    #         current = current.next
    #     return head
    
    def brute_using_map(self,head):
        if head is None or head.next is None:
            return False
        nodeMap ={}
        temp = head
        while temp is not None:
            if temp in nodeMap:
                return True
            nodeMap[temp] = 1
            temp = temp.next
        return False
    def optimal_using_Floyd_s_Cycle_Detection_Algorithm(self, head): # Tortoise and Hare Algorithm
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False 

    
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
    # Create a loop
    fifth.next = third

    sol = Solution(0)
    print(sol.brute_using_map(head))
    print(sol.optimal_using_Floyd_s_Cycle_Detection_Algorithm(head))
   