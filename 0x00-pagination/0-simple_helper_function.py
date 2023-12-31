#!/usr/bin/env python3
"""
Helper function
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Takes two integer arguments page and page_size

    Returns a tuple of size two containing a start index,
    and an end index corresponding to the range of indexes,
    To return in a list for those particular pagination,
    Parameters
    """
    return ((page - 1) * page_size, page * page_size)
