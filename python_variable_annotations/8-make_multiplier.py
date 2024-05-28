#!/usr/bin/env python3
"""Complex types - functions"""


from typing import Callable, Iterator, Union, Optional, List, Tuple


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""

    def multiply(n: float) -> float:
        """Return product of multiplier and n"""
        return n * multiplier

    return multiply
