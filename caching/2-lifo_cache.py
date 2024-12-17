#!/usr/bin/env python3
"""
class LIFOCache that inherits from BaseCaching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system"""
    def __init__(self):
        """ Initialize class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Method inerited from BaseCaching. Puts key and item in cache_data"""
        if key and item:
            self.cache_data[key] = item
            self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.order.pop(-2)
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """Method inerited from BaseCaching. Returns the value linked to key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
