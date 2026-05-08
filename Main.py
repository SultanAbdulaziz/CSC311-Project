class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def addTwoNumbers(l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    s1 = []
    s2 = []
    result = []
    for item in l1:
        s1.append(item)
    for item in l2:
        s2.append(item)

    ite = max(len(s1),len(s2))
    remainder = 0
    for i in ite:
        if len(s1) > len(s2):
            result.insert(s1.pop(),0)
        elif len(s2) > len(s1):
            result.insert(s2.pop(),0)
        else:
            result.insert(s1.pop() + s2.pop())



print(addTwoNumbers([],[]))  # Expected: 5
