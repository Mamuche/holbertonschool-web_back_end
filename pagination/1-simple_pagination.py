#!/usr/bin/env python3
"""Implement a method named get_page that takes two integer arguments page with
default value 1 and page_size with default value 10."""
from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> tuple:
    """return a tuple of size two containing a start index and an end index"""
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return the appropriate page of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start_idx, end_idx = index_range(page, page_size)

        dataset = self.dataset()
        if start_idx >= len(dataset):
            return []

        return self.dataset()[start_idx:end_idx]
