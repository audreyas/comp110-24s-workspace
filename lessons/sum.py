""""Summing the elements of a list using different loops"""

__author__= 730387535

def w_sum(vals: list[float]):
    """Summing the elements of a list using while loop"""
    sum = 0.0
    idx = 0 
    while idx < len(vals): 
        sum += vals[idx]
        idx += 1
    
    return sum 


def f_sum(vals: list[float]):
    """Summing the elements of a list using for ... in ... loop """
    sum = 0.0 
    for elem in vals:
        sum += elem

    return sum


def f_sum_range(vals: list[float]):
    """Summing the elements of a list using for ... in range(...) loop."""
    sum = 0.0 
    for idx in range(0,len(vals)):
        sum += vals[idx]

    return sum 