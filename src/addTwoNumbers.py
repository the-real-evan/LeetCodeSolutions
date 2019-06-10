# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        list1 = list()
        list2 = list()
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        num1 = ""
        num2 = ""
        for item in list1:
            num1 = str(item) + num1
        for item in list2:
            num2 = str(item) + num2
        sum = int(num1) + int(num2)
        solution = list(str(sum))
        root = ListNode(0)
        l3 = root
        for item in solution:
            l3.next = ListNode(int(item))
            l3 = l3.next
        return root.next

list1 = ListNode(2)
list1.next = ListNode(4)
list1.next.next = ListNode(3)
list2 = ListNode(5)
list2.next = ListNode(6)
list2.next.next = ListNode(4)
list2.next.next.next = ListNode(7)
sol = Solution.addTwoNumbers(list1, list2)
while sol:
    print(sol.val)
    sol = sol.next