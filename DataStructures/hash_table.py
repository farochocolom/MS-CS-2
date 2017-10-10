#!python

from linkedList import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table"""
        all_values = []
        for bucket in self.buckets:
            print("bucket:" + str(bucket))
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table"""
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        count = 0
        for bucket in self.buckets:
            count += len(bucket.items())
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        key_hash = self._bucket_index(key)

        if self.buckets[key_hash] is not None:
            node = self.buckets[key_hash]
            if node.head.data[0] == key:
                return True
            else:
                return False


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        key_hash = self._bucket_index(key)

        if self.buckets[key_hash] is not None:
            node = self.buckets[key_hash]
            if not node.is_empty() and node.head.data[0] == key:
                return node.head.data[1]
            else:
                raise KeyError('Key does not exist')

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        key_hash = self._bucket_index(key)
        key_value = key, value
        if self.buckets[key_hash].is_empty():
            self.buckets[key_hash] = LinkedList([key_value])
        else:
            if self.contains(key):
                self.buckets[key_hash].head.data = (key, value)
            else:
                self.buckets[key_hash].append(key_value)

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
