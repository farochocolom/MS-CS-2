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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            tmp = self.head
            while tmp.next is not None:
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
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if current is None:
            raise ValueError("Data not in list")

        if current.next is None:
            self.tail = previous

        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

        # if self.head is None:
        #     raise ValueError("List is empty")
        #
        # if self.head.data is item:
        #     if self.head.next is not None:
        #         self.head = self.head.next
        #     else:
        #         self.head = None
        #
        # previous = None
        # current = self.head
        #
        # while current is not None and current.data is not item:
        #     # if current_node.data is item:
        #     previous = current
        #     current = current.next
        #
        # if current is None:
        #     raise ValueError("Item was not found")
        #
        # previous.next = current.next

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality"""
        # TODO: find item where quality(item) is True
        for item in self.items():
            if quality(item):
                return item

        return None

    def _find_node(self, item):
        """Find and return a specific Node"""
        pass



def test_linked_list():
    ll = LinkedList()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    print('head: ' + str(ll.head))
    print('tail: ' + str(ll.tail))
    print('length: ' + str(ll.length()))
    print(ll.items())

    # Enable this after implementing delete:
    ll = LinkedList()
    ll.append('A')
    ll.append('B')
    ll.append('C')
    ll.delete('A')
    print(ll)
    print(ll.head.data == 'B')
    print(ll.tail.data == 'C')
    ll.delete('C')
    print(ll)
    print(ll.head.data == 'B')
    print(ll.tail.data == 'B')
    ll.delete('B')
    print(ll)
    print(ll.head is None)
    print(ll.tail is None)
    # with self.assertRaises(ValueError):
    #     ll.delete('D')


if __name__ == '__main__':
    test_linked_list()
