class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    Implement this.
    """

    def __init__(self, capacity):
        if capacity < MIN_CAPACITY:
            self.capacity = MIN_CAPACITY
        else:
            self.capacity = capacity

        self.storage = [None] * self.capacity
        self.size = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)
        One of the tests relies on this.
        Implement this.
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        Implement this.
        """
        return self.count / self.capacity


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        Implement this, and/or DJB2.
        """

        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        #FNV-1a Hash Function
        hash_val = offset_basis
        key_bytes = key.encode()

        for byte in key_bytes:
            hash_val = hash_val * FNV_prime
            hash_val = hash_val ^ byte

        return hash_val


    def djb2(self, key):
        """
        DJB2 hash, 32-bit
        Implement this, and/or FNV-1.
        """
        hash_val = 5381
        key_bytes = key.encode()
        for byte in key_bytes:
            hash_val = (( hash_val << 5) + hash_val) + byte
        return (hash_val & 0xFFFFFFFF) # 0xFFFFFFFF means: take only the right-most 8 digits


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Implement this.
        """
        # 1. Hash the key
        # 2. Take the hash and mod it with len of array
        idx = self.hash_index(key)
        # 3a. Check if there is a collision
        if self.storage[idx] != None:
            # Check if the key is already in linked list
            node = self.storage[idx] # This is the head of the linked list
            while node is not None:
                if node.key == key:
                ## If so, update the value 
                    node.value = value
                    return
                node = node.next

                ## If not, add a node to the head of the linked list
                old_head = self.storage[idx]
                new_head = HashTableEntry(key, value)
                new_head.next = old_head
                self.storage[idx] = new_head
                
        # 3b. Go to index and put in value
        else:
            # Add the first node
            self.storage[idx] = HashTableEntry(key, value)


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Implement this.
        """
        # Find index for given key
        idx = self.hash_index(key)
        # Set index to None
        self.storage[idx] = None


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Implement this.
        """
        # 1. Hash the key
        # 2. Take the hash and mod it with len of array
        idx = self.hash_index(key)
        # 3. Go to index and get traverse our linked list
        node = self.storage[idx]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        Implement this.
        """
        prev_table = self.storage[:]
        prev_capacity = self.capacity
        self.capacity = new_capacity
        new_table  = [None] * self.capacity
        

        # Add the values to new table
        for idx in range(prev_capacity):
            if prev_table[idx] is not None:
                entry = prev_table[idx]
                new_table.put(entry.key, entry.value)



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
