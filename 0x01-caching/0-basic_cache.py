#!/usr/bin/env python3
"""
Class BasicCache
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class BasicCache defination
    """
    def put(self, key, item):
        """
        Updates an item
        In the cache
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        Else return None
        """
        return self.cache_data.get(key)
