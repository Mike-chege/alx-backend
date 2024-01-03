#!/usr/bin/env python3
"""
LRU Caching
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    Class LRUCache
    Definition
    """
    def __init__(self):
        """
        Initialize class instance
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Update an item
        In the cache
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(discarded[0]))

    def get(self, key):
        """
        Get an
        Item by key
        """
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
