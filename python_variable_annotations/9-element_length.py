#!/usr/bin/env python3
"""Lets duck type an iterable object"""
from typing import List, Tuple, Sequence, Iterable, Mapping, MutableMapping


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Element length function"""
    return [(i, len(i)) for i in lst]
