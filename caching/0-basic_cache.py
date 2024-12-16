#!/usr/bin/env python3
"""
class BasicCache that inherits from BaseCaching
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching system without limit"""
    def put(self, key, item):
        """Method inerited from BaseCaching. Puts key and item in cache_data"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """Method inerited from BaseCaching. Returns the value linked to key"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
