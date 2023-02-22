#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initialize
        """
        super().__init__()
        self.key_list = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            if self.key_list:
                first_key = self.key_list[0]
                del self.cache_data[first_key]
                print("DISCARD: {}".format(first_key))
                self.key_list.pop(0)

        self.cache_data[key] = item
        self.key_list.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
