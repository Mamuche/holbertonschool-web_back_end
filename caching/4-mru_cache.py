#!/usr/bin/env python3
"""
class MRUCache that inherits from BaseCaching
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU caching system"""
    def __init__(self):
        """ Initialize class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Method inerited from BaseCaching. Puts key and item in cache_data"""
        if key and item:
            if key in self.order:
                self.order.remove(key)
            self.order.append(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(-2)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """Method inerited from BaseCaching. Returns the value linked to key"""
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
