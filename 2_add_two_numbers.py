# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def __init__(self):
        self.dummy = None
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.dummy.next
        while node:
            yield node
            node = node.next

    def addTwoNumbers(self, l1, l2):
        self.dummy = ListNode(0)
        cur = self.dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val %= 10

            # add to the current node
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next

            # move to the next node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return self.dummy.next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def add(self, node):
        if self.head:
            self.tail.next = node
        else:
            self.head = node

        self.tail = node


if __name__ == "__main__":
    instance1 = Solution()

    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    print("Case 1:")
    print(instance1.addTwoNumbers(l1, l2).val)
    print(instance1.addTwoNumbers(l1, l2).next.val)
    print(instance1.addTwoNumbers(l1, l2).next.next.val)

    print("Case 2:")

    l1 = ListNode(0)
    l2 = ListNode(0)
    instance1.addTwoNumbers(l1, l2)
    print([node.val for node in instance1])

    print("Case 3:")

    l1 = LinkedList()
    l1.add(ListNode(9))
    l1.add(ListNode(9))
    l1.add(ListNode(9))
    l1.add(ListNode(9))
    l1.add(ListNode(9))
    l1.add(ListNode(9))
    l1.add(ListNode(9))
    print([node.val for node in l1])

    l2 = LinkedList()
    l2.add(ListNode(9))
    l2.add(ListNode(9))
    l2.add(ListNode(9))
    l2.add(ListNode(9))
    print([node.val for node in l2])

    instance1.addTwoNumbers(l1.head, l2.head)
    print([node.val for node in instance1])
