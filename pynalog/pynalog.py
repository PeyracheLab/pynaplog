# -*- coding: utf-8 -*-
"""Test for pynalog
"""
# @Author: gviejo
# @Date:   2022-08-15 22:29:59
# @Last Modified by:   gviejo
# @Last Modified time: 2022-08-24 11:43:01
import numpy as np


def test():
    """Summary
    Returns
    -------
    TYPE
        Description
    """
    print("pynalog")


def plogsum(nmg):
    """Summary

    Parameters
    ----------
    nmg : TYPE
        Description

    Returns
    -------
    TYPE
        Description
    """
    my_sum = np.sum(np.random.rand(nmg))
    return my_sum


def coding_club(name):
    """Summary

    Parameters
    ----------
    name : TYPE
        Description

    Returns
    -------
    TYPE
        Description
    """
    print(name)

    # b_adrien = 0

    # if b_adrien == 1:
    #     print("sofia")

    for i in range(10):
        for j in range(100):
            for k in range(20):
                print(i, j, k)

    return True
