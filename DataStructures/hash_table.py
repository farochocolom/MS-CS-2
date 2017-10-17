#!python

from linkedList import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):    # Linear time
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]
        # List comprehension with empty LinkedList initializer, linear time

    def __str__(self):  # linear time
        """Return a formatted string representation of this hash table"""
        # list comprehension for items in hash table, linear time
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]

        # String joining, linear time
        return '{' + ', '.join(items) + '}'

    def __repr__(self):     # linear time
        """Return a string representation of this hash table"""
        # Return all the items in the hash table in a string representation, linear time
        return 'HashTable({})'.format(repr(self.items()))

    # def __iter__(self):
    #     current = self.buckets[0]
    #     for index in range(0, self.length()):
    #         yield current
    #         current = current[index+1]
    #         print(current)

    def _bucket_index(self, key):   # constant time
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)
        # both hash and len are constant time.
        # In python, a list knows it's own length

    def keys(self):     # n^2 time
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        all_keys = []   # create empty list, constant time
        for bucket in self.buckets:     # iterate through every bucket, linear time
            for key, value in bucket.items():   # iterate through every tuple in the bucket, linear time
                all_keys.append(key)    # append to the list, constant time
        return all_keys     # return all_keys list, constant times

    def values(self):   # n^2 time
        """Return a list of all values in this hash table"""
        all_values = []     # create empty list, constant time
        for bucket in self.buckets:     # iterate through every bucket, linear time
            for key, value in bucket.items():   # iterate through every tuple in the bucket, linear time
                all_values.append(value)     # append to the list, constant time
        return all_values   # return all_values list, constant times

    def items(self):    # linear time
        """Return a list of all items (key-value pairs) in this hash table"""
        all_items = []  # create empty list, constant time
        for bucket in self.buckets:     # iterate through every bucket, linear time
            all_items.extend(bucket.items())    # append to the list, constant time
        return all_items    # return all_items list, constant times

    def length(self):   # linear time
        """Return the length of this hash table by traversing its buckets"""
        count = 0   # create and set count variable to 0, constant time
        for bucket in self.buckets:     # iterate through every bucket, linear time
            count += len(bucket.items())    # add 1 to count, constant time
        return count    # return count, constant time

    def contains(self, key):    # constant time
        """Return True if this hash table contains the given key, or False"""
        key_hash = self._bucket_index(key)  # bucket_index is constant time, this is constant time
        bucket = self.buckets[key_hash]  # bucket_index is constant time, this is constant time
        key_found = bucket.find(lambda item: item[0] == key)  # linear time
        if key_found:
            return True
        return False    # constant time

    def get(self, key):  # linear time
        """Return the value associated with the given key, or raise KeyError"""
        key_hash = self._bucket_index(key)  # bucket_index is constant time, this is constant time
        bucket = self.buckets[key_hash]  # bucket_index is constant time, this is constant time
        key_found = bucket.find(lambda item: item[0] == key)  # linear time
        if key_found:
            return key_found[1]
        raise KeyError('Key does not exist')    # constant time
        # current_node = bucket.head
        #
        # while current_node is not None:
        #     if current_node.data[0] == key:
        #         return current_node.data[1]

        # if self.buckets[key_hash] is not None:  # check if the index is empty, constant time
        #     bucket = self.buckets[key_hash]   # set bucket to the index value, constant time
        #     # check if bucket is empty, and that the key is equal to the bucket data, constant time
        #     if not bucket.is_empty() and bucket.head.data[0] == key:
        #         return bucket.head.data[1]    # constant time
        #     else:
        #         raise KeyError('Key does not exist')    # constant time


    def set(self, key, value):  # constant time, O(1)
        """Insert or update the given key with its associated value"""
        key_hash = self._bucket_index(key)  # set the key hash to the bucket index
        key_value = key, value  # set the key value to a tuple containing the key and value
        if self.buckets[key_hash].is_empty():  # check if empty, O(1)
            self.buckets[key_hash] = LinkedList([key_value]) # set value, constant time
        else:
            if self.contains(key):  # check if contains, constant time
                self.buckets[key_hash].head.data = (key, value)  # set value, constant time
            else:
                self.buckets[key_hash].append(key_value)  # Append, constant time

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        key_to_delete = self.get(key)
        key_hash = self._bucket_index(key)
        self.buckets[key_hash].delete((key, key_to_delete))


def test_hash_table():
    ht = HashTable()
    print(ht)

    print('Setting entries:')
    ht.set('I', 1)
    print(ht)
    ht.set('V', 5)
    print(ht)
    ht.set('X', 10)
    print(ht)

    print('contains(X): ' + str(ht.contains('X')))
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('length: ' + str(ht.length()))

    for item in ht:
        print(ht[item])

    # Enable this after implementing delete:
    print('Deleting entries:')
    ht.delete('I')
    print(ht)
    ht.delete('V')
    print(ht)
    ht.delete('X')
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('length: ' + str(ht.length()))


if __name__ == '__main__':
    test_hash_table()
