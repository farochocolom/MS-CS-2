#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any"""
        self.head = None
        self.tail = None

        if iterable:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list"""
        items = ['({})'.format(repr(item)) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(repr(self.items()))

    def items(self):
        """Return a list of all items in this linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes"""
        if self.head is None:
            return 0
        else:
            current_node = self.head
            count = 1
            while current_node.next is not None:
                current_node = current_node.next
                count += 1
            return count


    def append(self, item):
        """Insert the given item at the tail of this linked list"""
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next

            tmp.next = Node(item)
            self.tail = Node(item)

    def prepend(self, item):
        """Insert the given item at the head of this linked list"""
        if self.head is None:
            self.head = Node(item)
            self.tail = self.head
        else:
            tmp = self.head
            self.head = Node(item)
            self.head.next = tmp


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError"""
        # TODO: find given item and delete if found
        pass

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # TODO: find item where quality(item) is True
        for item in self.items():
            if quality(item):
                return item

        return "no item that meets the criteria was found"


def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    ll.prepend('x')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print('length: ' + str(ll.length()))
    print(ll.items())

    # ll = LinkedList()
    # ll.append('A')
    # ll.append('B')
    # ll.append('C')
    # assert ll.find(lambda item: item == 'B') == 'B'
    # assert ll.find(lambda item: item < 'B') == 'A'
    # assert ll.find(lambda item: item > 'B') == 'C'
    # assert ll.find(lambda item: item == 'D') is None

    # Enable this after implementing delete:
    # print('Deleting items:')
    # ll.delete('B')
    # print(ll)
    # ll.delete('C')
    # print(ll)
    # ll.delete('A')
    # print(ll)
    # print('head: ' + str(ll.head))
    # print('tail: ' + str(ll.tail))
    # print('length: ' + str(ll.length()))


if __name__ == '__main__':
    test_linked_list()


