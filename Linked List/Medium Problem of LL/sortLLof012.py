class Solution:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    
    @staticmethod
    def arrToLL(arr):
        if not arr:
            return None
        head = Solution(arr[0])
        current = head
        for value in arr[1:]:
            current.next = Solution(value)
            current = current.next
        return head
    
    def brute(self,head):
        if head is None or head.next is None:
            return head
        
        cnt0 = cnt1 = cnt2 = 0

        temp = head
        while temp:
            if temp.data == 0:
                cnt0+=1
            elif temp.data == 1:
                cnt1+=1
            else:
                cnt2+=1
            temp = temp.next
        
        temp = head
        while temp:
            if cnt0:
                temp.data = 0
                cnt0-=1
            elif cnt1:
                temp.data = 1
                cnt1-=1
            else:
                temp.data = 2
                cnt2-=1
            temp = temp.next
        
        return head
    
    def optimal(self,head):
        if head is None or head.next is None:
            return head
        
        zeroHead = Solution(-1)
        oneHead = Solution(-1)
        twoHead = Solution(-1)
        zero = zeroHead
        one = oneHead
        two = twoHead

        temp = head

        while temp:
            if temp.data == 0:
                zero.next = temp
                zero = zero.next
                
            elif temp.data == 1:
                one.next = temp
                one = one.next

            else:
                two.next = temp
                two = two.next
            temp = temp.next
        
        # connect List:
        zero.next = oneHead.next if oneHead.next else twoHead.next
        one.next = twoHead.next
        two.next = None

        return zeroHead.next




if __name__ == "__main__":
    arr = [2,1,0,1,0,2,0,2,0]
    head = Solution.arrToLL(arr=arr)
    sol = Solution(0)
    # brute = sol.brute(head)
    optimal = sol.optimal(head=head)

    temp = optimal
    while temp :
        print(temp.data , end=' -> ')
        temp = temp.next
    print('None')