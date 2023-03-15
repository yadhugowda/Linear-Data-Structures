class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next

    def printLinkedlist(self):
        print(self.value, end=' ')

        if self.next:
            self.next.printLinkedlist()
        else:
            print()

    def lengthLinkedlist(self):
        count = 1

        if self.next:
            count += self.next.lengthLinkedlist()

        return count
    def reverseLinkedList(self, length):
        head, rest = self, self.next

        if length > 1:
            if rest:
                head, rest = rest.reverseLinkedList(length - 1)

                self.next.next = self
                self.next = None

        return head, rest

    def reverseGroups(self):
        head = self
        length = self.lengthLinkedlist()

        if length > 3:
            tail = self
            head, rest = self.reverseLinkedList(length//2)  # left

            if length % 2 == 1:  # odd, skip over middle
                tail.next = rest
                tail = tail.next
                rest = tail.next
                tail.next, _ = rest.reverseLinkedList(length//2)  # right

        return head

if __name__ == '__main__':

    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)

    print('original linked list is: ', end='')
    head.printLinkedlist()

    head = head.reverseGroups()
