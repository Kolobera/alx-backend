#!/usr/bin/env python3
"""Task 4's module.
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A MRUCache class.
    """
    def __init__(self):
        """Initializes the MRUCache class.
        """
        super().__init__()
        self.mru = []

    def put(self, key, item):
        """Adds a key-value pair to the cache.
        """
        if key and item:
            if key in self.cache_data:
                self.mru.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(self.mru[-1]))
                del self.cache_data[self.mru[-1]]
                self.mru.pop()
            self.cache_data[key] = item
            self.mru.insert(0, key)

    def get(self, key):
        """Gets a value from the cache.
        """
        if key in self.cache_data:
            self.mru.remove(key)
            self.mru.insert(0, key)
        return self.cache_data.get(key)
