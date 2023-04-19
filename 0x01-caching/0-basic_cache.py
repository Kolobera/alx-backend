#!/usr/bin/env python3
"""Task 0's module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A BasicCache class.
    """
    def put(self, key, item):
        """Adds a key-value pair to the cache.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Gets a value from the cache.
        """
        return self.cache_data.get(key)
