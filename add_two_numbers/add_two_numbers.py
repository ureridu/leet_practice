# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        num = int(''.join([str(i) for i in l1[::-1]])) + int(''.join([str(i) for i in l2[::-1]]))
        return [s for s in str(num)][::-1]




if __name__ == '__main__':
    s = Solution()
    print(s.addTwoNumbers([0, 1, 2], [3, 4, 5]))
    print(s.addTwoNumbers([0], [0]))
    print(s.addTwoNumbers([9,9,9,9,9,9,9], [9,9,9,9]))