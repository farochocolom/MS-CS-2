from __future__ import division, print_function


class Listogram(list):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new list; update with given items"""
        super(Listogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            if self.__contains__(item):
                self.tokens += 1
                word_index = self._index(item)
                current_item = self.pop(word_index)
                current_count = current_item[1] + 1
                self.insert(word_index, (item, current_count))
            else:
                self.tokens += 1
                self.types += 1
                self.append((item, 1))

        print(self)

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        # TODO: retrieve item count
        if any(item in code for code in self):
            word_index = self._index(item)
            current_item = self[word_index]
            current_count = current_item[1]
            return current_count

        return 0

    def __contains__(self, item):
        """Return True if the given item is in this histogram, or False"""
        # TODO: check if item is in histogram
        if any(item in code for code in self):
            return True

        return False

    def _index(self, target):
        """Return the index of the (target, count) entry if found, or None"""
        # TODO: implement linear search to find an item's index
        indices = next((i for i, v in enumerate(self) if v[0] == target), -1)
        return indices