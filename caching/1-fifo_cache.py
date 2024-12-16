#!/usr/bin/env python3
"""
class FIFOCache that inherits from BaseCaching
"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """FIFO caching system"""
    def __init__(self):
        """ Initialize class """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Method inerited from BaseCaching. Puts key and item in cache_data"""
        if key and item:
            self.order.append(key)
            self.cache_data[key] = item
        
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """Method inerited from BaseCaching. Returns the value linked to key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
    