#!/usr/bin/env python3
"""
Caching System
"""


class FIFOCache(BaseCaching):
    """
    ClassFIFO
    Caching system
    """
    def __init__(self):
        """
        Initialize
        Class instance
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
            discarded_key = sorted(self.cache_data)[0]
            self.cache_data.pop(discarded_key)
            print('DISCARD: {}'.format(discarded_key))

    def get(self, key):
        """
        Gets an
        Item by key
        """
        return self.cache_data.get(key)
