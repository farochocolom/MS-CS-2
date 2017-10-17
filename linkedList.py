#!python

from __future__ import print_function


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data"""
        self.data = data    # Set variable, constant time
        self.next = None    # Set variable, constant time

    def __repr__(self):
        """Return a string representation of this node"""
        return 'Node({})'.format(repr(self.data))  # format string, constant time


class LinkedList(object):

    def __init__(self, iterable=None):  # linear^2 time
        """Initialize this linked list; append the given items, if any"""
        self.head = None    # Set variable, constant time
        self.tail = None    # Set variable, constant time
        self.count = 0

        if iterable:    # check condition, constant time
            for item in iterable:   # for loop for each item in iterable, linear time
                self.append(item)   # append to a linked list, linear time

    def __str__(self):      # constant time
        """Return a formatted string representation of this linked list"""
        items = ['({})'.format(repr(item)) for item in self.items()]  # list comprehension, linear time
        return '[{}]'.format(' -> '.join(items))  # format string, constant time

    def __repr__(self):     # constant time
        """Return a string representation of this linked list"""
        return 'LinkedList({})'.format(repr(self.items()))  # format string, constant time

    def __iter__(self):     #linear time
        # Remember, self is our UnorderedList.
        # In order to get to the first Node, we must do
        current = self.head  # Set variable, constant time
        # and then, until we have reached the end:
        while current is not None:  # while loop, worst case is O(n)
            yield current   # create an iterator generator, constant time
            # in order to get from one Node to the next one:
            current = current.next  # Set variable, constant time

    def items(self):  # linear time
        """Return a list of all items in this linked list"""
        result = []     # create an empty list, linear time
        current = self.head     # Set variable, linear time
        while current is not None:      # while loop, worst case is linear time
            result.append(current.data)     # append to a list, constant time
            current = current.next      # Set variable, constant time
        return result   # return a list, constant time

    def is_empty(self):     # constant time
        """Return True if this linked list is empty, or False"""
        return self.head is None    # comparing head to none and returning a boolean, linear time

    def length(self):       # linear time
        """Return the length of this linked list by traversing its nodes"""
        if self.head is None:   # comparing head to none, constant time
            return 0    # returning 0, constant time
        else:
            current_node = self.head                # set current_node to the head, constant time
            count = 1                               # set count to 1, constant time
            while current_node.next is not None:    # iterate until current_node.next is equal to none, linear time
                current_node = current_node.next    # set current_node to current_node.next, constant time
                count += 1                          # add one to the count, constant time
            return count                            # return count, constant time

    def append(self, item):     # constant time
        """Insert the given item at the tail of this linked list"""
        new_node = Node(item)               # set new_node to a new Node instance, constant time
        if self.head is None:               # comparing head to None, constant time
            self.head = new_node            # set head to new_node, constant time
        else:
            self.tail.next = new_node       # set tmp.next to a Node of item, constant time
        self.tail = new_node                # set tail to the Node(item), constant time

    def enqueue(self, item):     # constant time
        """Insert the given item at the tail of this linked list"""
        new_node = Node(item)               # set new_node to a new Node instance, constant time
        if self.head is None:               # comparing head to None, constant time
            self.head = new_node            # set head to new_node, constant time
        else:
            self.tail.next = new_node       # set tmp.next to a Node of item, constant time
        self.tail = new_node                # set tail to the Node(item), constant time
        self.count += 1

    def dequeue(self):
        word_to_return = ""
        if self.head is None:
            raise LookupError("Head is empty, can't dequeue")
        else:
            word_to_return = self.head
            self.head = self.head.next
        self.count -= 1
        return word_to_return

    def prepend(self, item):    # constant time
        """Insert the given item at the head of this linked list"""
        if self.head is None:       # compare head to None, constant time
            self.head = Node(item)  # set head to Node of item, constant time
            self.tail = self.head   # set tail to head, constant time
        else:
            tmp = self.head         # set tmp to head, constant time
            self.head = Node(item)  # set head to Node(item), constant time
            self.head.next = tmp    # set head.next to tmp, constant time

    def delete(self, item):     # linear time
        """Delete the given item from this linked list, or raise ValueError"""
        # TODO: find given item and delete if found
        current = self.head                         # set current to head, constant time
        previous = None                             # set previous to None, constant time
        found = False                               # set found to False, constant time
        while current and found is False:           # iterate until found is true and current doesn't exist, linear time
            if current.data == item:                # compare current.data to the item, constant time
                found = True                        # set found to true, constant time
            else:
                previous = current                  # set prevous to current, constant time
                current = current.next              # set current to current.next, constant time
        if current is None:                         # check if current is none, constant time
            raise ValueError("Data not in list")    # raiser error, constant time

        if current.next is None:                    # check that current is None, constant time
            self.tail = previous                    # set tail to previous node, constant time

        if previous is None:                        # check that previous is None, constant time
            self.head = current.next                # set head to the next node of current node, constant time
        else:
            previous.next = current.next            # set next node of previous node to the next node of current node, constant time

    def find(self, quality):    # linear time
        """Return an item from this linked list satisfying the given quality"""
        items = self.items()
        for item in items:   # iterate through all items in the linked list, linear time
            if quality(item):       # check that quality(item) is true, constant time
                return item         # return item, constant time

        return None                 # return None, constant time


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

    for thing in ll:
        print("things: " + str(thing))

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
