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
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset (i.e. the correct
        list of rows).
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        if start >= len(self.dataset()):
            return []
        return self.dataset()[start:end]
    
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return a dictionary containing the following key-value pairs:
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        return {
            "page_size": page_size,
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": page + 1 if (page * page_size) < len(self.dataset()) else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": math.ceil(len(self.dataset()) / page_size)
        }
