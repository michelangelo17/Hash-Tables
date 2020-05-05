class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1a 64-bit hash function

        Implement this, and/or DJB2.
        """

        offset_basis_64 = 14695981039346656037
        FNV_prime_64 = 1099511628211

        key_bytes = key.encode()

        hash = offset_basis_64

        for k_byte in key_bytes:
            hash ^= k_byte
            hash *= FNV_prime_64
            hash &= 0xffffffffffffffff
        return hash

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        key_bytes = key.encode()
        hash = 5381
        for k_byte in key_bytes:
            hash = hash * 33 + k_byte
            hash &= 0xffffffff
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """

        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """

        key_index = self.hash_index(key)
        cur_node = self.storage[key_index]

        if not cur_node:
            self.storage[key_index] = HashTableEntry(key, value)
            return

        while cur_node:
            if cur_node.key == key:
                cur_node.value = value
                return
            elif not cur_node.next:
                cur_node.next = HashTableEntry(key, value)
                return
            else:
                cur_node = cur_node.next

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        key_index = self.hash_index(key)

        cur_node = self.storage[key_index]

        if cur_node.key == key:
            self.storage[key_index] = cur_node.next
            cur_node.next = None
            return

        while cur_node.next:
            if cur_node.next.key == key:
                delete_node = cur_node.next
                cur_node.next = delete_node.next
                delete_node.next = None
                return
            else:
                cur_node = cur_node.next
        return print('Key not found!')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        key_index = self.hash_index(key)

        cur_node = self.storage[key_index]

        while cur_node:
            if cur_node.key == key:
                return cur_node.value
            else:
                cur_node = cur_node.next
        return cur_node

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """


if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    # old_capacity = len(ht.storage)
    # ht.resize()
    # new_capacity = len(ht.storage)

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    # print(ht.delete('line_2'))
    # # Test if data intact after resizing
    # print(ht.get("line_1"))
    # print(ht.get("line_2"))
    # print(ht.get("line_3"))

    # print(ht.storage)
