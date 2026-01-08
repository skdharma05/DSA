class Node:
    def __init__(self , data, next = None):
        self.data = data
        self.next = next

    @staticmethod
    def array_to_linked_list(arr): 
        if not arr:
            return None
        
        head =  Node(arr[0])
        current = head

        for value in arr[1:]:
            current.next = Node(value)
            current = current.next
        return head
    @staticmethod
    def lengthOfLinkList(head):
        count =0
        temp = head
        while temp:
            temp = temp.next
            count+=1
        return count



if __name__ == "__main__":
    arr = [1,2,3,4,5]
    head = Node.array_to_linked_list(arr)
    length = Node.lengthOfLinkList(head)
    print(length)
    # temp = head
    # while temp:
    #     print(temp.data , end=" ")
    #     temp = temp.next
         














    # y = Node(arr[2])
    # x = Node(arr[1])
    # print(y.data)
    # print(y.next.data)
        