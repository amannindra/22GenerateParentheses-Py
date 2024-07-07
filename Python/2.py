class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        numS1 = ""
        numS2 = ""
        while(l1):
            numS1 += str(l1.val)
            l1 = l1.next
        while(l2):
            numS2 += str(l2.val)
            l2 = l2.next
        output = int(numS1) + int(numS2)
        s = ListNode(output)
        print(s)
        return s