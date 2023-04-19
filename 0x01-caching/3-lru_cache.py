#!/usr/bin/env python3
"""Task 3's module.
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A LRUCache class.
    """
    def __init__(self):
        """Initializes the class.
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Adds a key-value pair to the cache.
        """
        if key and item:
            if key in self.keys:
                self.keys.remove(key)
            self.keys.append(key)
            self.cache_data[key] = item
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                last = self.keys.pop(0)
                del self.cache_data[last]
                print("DISCARD: {}".format(last))

    def get(self, key):
        """Gets a value from the cache.
        """
        if key in self.keys:
            self.keys.remove(key)
            self.keys.append(key)
        return self.cache_data.get(key)
