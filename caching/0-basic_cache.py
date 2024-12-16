#!/usr/bin/env python3
"""
class BasicCache that inherits from BaseCaching
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """"""
    def put(self, key, item):
        """"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None