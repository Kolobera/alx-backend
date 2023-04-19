#!/usr/bin/env python3
"""Task 2's module.
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A LIFOCache class.
    """
    def __init__(self):
        """Initializes the LIFOCache class.
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Adds a key-value pair to the cache.
        """
        if key and item:
            if key in self.cache_data:
                self.keys.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                last = self.keys.pop()
                print("DISCARD: {}".format(last))
                del self.cache_data[last]
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """Gets a value from the cache.
        """
        return self.cache_data.get(key)
