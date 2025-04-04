#!/usr/bin/env python3
""" Create class Cache """

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """ Store an instance of the Redis client """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
