#!/usr/bin/env python3
"""Task 2's module.
"""
from typing import List, Tuple, Dict
import math
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    data = []

    def __init__(self):
        """Initialize the server.
        """
        with open('Popular_Baby_Names.csv') as f:
            reader = csv.reader(f)
            next(reader)
            self.data = [row for row in reader]

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset (i.e. the correct
        list of rows).
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        if start >= len(self.data):
            return []
        return self.data[start:end]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return a dictionary containing the following key-value pairs:
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        if start >= len(self.data):
            return {}
        return {
            "page_size": len(self.data[start:end]),
            "page": page,
            "data": self.data[start:end],
            "next_page": page + 1 if end < len(self.data) else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": math.ceil(len(self.data) / page_size)
        }
