from __future__ import division, print_function


class Dictogram(dict):

    def __init__(self, word=None, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0  # the number of distinct item types in this histogram
        self.tokens = 0  # the total count of all item tokens in this histogram
        if iterable:
            self.update(iterable)
        if word:
            self.add(word)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            # TODO: increment item count
            if item in self:
                self.tokens += 1
                self[item] += 1
            else:
                self.tokens += 1
                self.types += 1
                self[item] = 1

    def add(self, word):
        if word in self:
            self.tokens += 1
            self[word] += 1
        else:
            self.tokens += 1
            self.types += 1
            self[word] = 1

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        # TODO: retrieve item count
        if item in self:
            return self[item]
        else:
            return 0

        pass
