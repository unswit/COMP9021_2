class Node:
    def __init__(self, value = None):
        self.value = value
        self.next_node = None
        self.previous_node = None


# 1->2->3->4->5.........->10000

# Node {
#    value
#    next_node
#    previous_node
# }

# LinkedNodeList
        # first/header
        # tail/last
        # length/count/total

# Node first = list1->first
# while first is not None:
#       print(first.value)
#       first = first->next_node










# Node
#    next_node
#    previous_node
# 1->2->3->4->5......->10

# LinkedList
    # first/header
    # tail/last
    # tail->next = 15
    # tail = tail->next
    # length/count/total


class DoublyLinkedList:
    def __init__(self, L = None):
        '''Creates an empty list or a list built from a subscriptable object.

        >>> DoublyLinkedList().print_from_head_to_tail()
        >>> DoublyLinkedList().print_from_tail_to_head()
        >>> DoublyLinkedList([]).print_from_head_to_tail()
        >>> DoublyLinkedList([]).print_from_tail_to_head()
        >>> DoublyLinkedList((0,)).print_from_head_to_tail()
        0
        >>> DoublyLinkedList((0,)).print_from_tail_to_head()
        0
        >>> DoublyLinkedList(range(4)).print_from_head_to_tail()
        0, 1, 2, 3
        >>> DoublyLinkedList(range(4)).print_from_tail_to_head()
        3, 2, 1, 0
        '''
        if L is None:
            self.head = None
            self.tail = None
            return
        # If L is not subscriptable, then will generate an exception that reads:
        # TypeError: 'type_of_L' object is not subscriptable
        if not len(L[: 1]):
            self.head = None
            self.tail = None
            return
        node = Node(L[0])
        self.head = node
        for e in L[1: ]:
            node.next_node = Node(e)
            node.next_node.previous_node = node
            node = node.next_node
        self.tail = node

    def print_from_head_to_tail(self):
        '''
        >>> DoublyLinkedList().print_from_head_to_tail()
        >>> DoublyLinkedList(range(1)).print_from_head_to_tail()
        0
        >>> DoublyLinkedList(range(2)).print_from_head_to_tail()
        0, 1
        >>> DoublyLinkedList(range(3)).print_from_head_to_tail()
        0, 1, 2
        '''
        if not self.head:
            return
        nodes = []
        node = self.head
        while node:
            nodes.append(str(node.value))
            node = node.next_node
        print(', '.join(nodes))

    def print_from_tail_to_head(self):
        '''
        >>> DoublyLinkedList().print_from_tail_to_head()
        >>> DoublyLinkedList(range(1)).print_from_tail_to_head()
        0
        >>> DoublyLinkedList(range(2)).print_from_tail_to_head()
        1, 0
        >>> DoublyLinkedList(range(3)).print_from_tail_to_head()
        2, 1, 0
        '''
        if not self.tail:
            return
        nodes = []
        node = self.tail
        while node:
            nodes.append(str(node.value))
            node = node.previous_node
        print(', '.join(nodes))

    def keep_every_second_element(self):
        '''
        >>> L = DoublyLinkedList(); L.keep_every_second_element()
        >>> L.print_from_head_to_tail()
        >>> L.print_from_tail_to_head()
        >>> L = DoublyLinkedList([1]); L.keep_every_second_element()
        >>> L.print_from_head_to_tail()
        1
        >>> L.print_from_tail_to_head()
        1
        >>> L = DoublyLinkedList([1, 2]); L.keep_every_second_element()
        >>> L.print_from_head_to_tail()
        1
        >>> L.print_from_tail_to_head()
        1
        >>> L = DoublyLinkedList([1, 2, 3]); L.keep_every_second_element()
        >>> L.print_from_head_to_tail()
        1, 3
        >>> L.print_from_tail_to_head()
        3, 1
        >>> L = DoublyLinkedList([1, 2, 3, 4]); L.keep_every_second_element()
        >>> L.print_from_head_to_tail()
        1, 3
        >>> L.print_from_tail_to_head()
        3, 1
        >>> L = DoublyLinkedList([1, 2, 3, 4, 5]); L.keep_every_second_element()
        >>> L.print_from_head_to_tail()
        1, 3, 5
        >>> L.print_from_tail_to_head()
        5, 3, 1
        '''
        # Insert your code here
        if self.head:
            node = self.head
            while node and node.next_node:
                node.next_node = node.next_node.next_node
                if node.next_node:
                    node.next_node.previous_node = node
                if not node.next_node:
                    self.tail = node
                node = node.next_node

if __name__ == '__main__':
    import doctest
    doctest.testmod()
