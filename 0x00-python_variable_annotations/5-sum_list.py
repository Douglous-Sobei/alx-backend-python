#!/usr/bin/env python3
"""
    List of floats annotations
"""
from typing import List


def sum_lis(input_list: List[float]) -> float:
    """
        Args:
            Input_list: float numbers

        Return:
            Sum of the float numbers
    """

    result: float = 0

    for i in input_list:
        result += i

    return result
