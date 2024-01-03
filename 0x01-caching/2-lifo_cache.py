#!/usr/bin/env python3
"""
LIFO Caching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Class LIFOcache
    """
    def __init__(self):
        """
        Initialize class instance
        """
        super().__init__()

    def put(self, key, item):
        """
        Update an item
        In the cache
        """
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            self.cache_data.pop(self.last_item)
            print('DISCARD:', self.last_item)
        if key:
            self.last_item = key

    def get(self, key):
        """
        Gets an
        Item by key
        """
        return self.cache_data.get(key)
